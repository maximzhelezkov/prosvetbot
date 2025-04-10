import sqlite3

conn = sqlite3.connect('prosvet.db')
cur = conn.cursor()

cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER UNIQUE,
            username TEXT
        )
    ''')

conn.commit()
conn.close()

def user_exists(user_id):
    conn = sqlite3.connect('prosvet.db')
    cur = conn.cursor()

    cur.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    result = cur.fetchone()

    conn.close()

    return result is not None

def db(user_id, username):
    conn = sqlite3.connect('prosvet.db')
    cur = conn.cursor()

    if user_exists(user_id):
        cur.execute('UPDATE users SET username = ? WHERE user_id = ?', (username, user_id))
    else:
        cur.execute('INSERT INTO users (user_id, username) VALUES (?, ?)', (user_id, username))

    conn.commit()
    conn.close()

