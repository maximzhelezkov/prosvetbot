import sqlite3

conn = sqlite3.connect('prosvet.db')
cur = conn.cursor()

cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER UNIQUE,
            username TEXT,
            name TEXT,
            phone INT, 
            selected_date STR,
            month STR,
            time_str STR

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

def db_add_info(name, phone, selected_date, time_str, user_id):
    # Используем контекстный менеджер для автоматического закрытия соединения
    with sqlite3.connect('prosvet.db') as conn:
        cur = conn.cursor()
        
        # Проверим, существует ли уже пользователь
        cur.execute('SELECT user_id FROM users WHERE user_id = ?', (user_id,))
        user = cur.fetchone()
        
        if user:
            # Если пользователь существует, обновим данные
            cur.execute('UPDATE users SET name = ?, phone = ?, selected_date = ?, time_str = ? WHERE user_id = ?',
                        (name, phone, selected_date, time_str, user_id))
        else:
            # Если пользователя нет, вставим новые данные
            cur.execute('INSERT INTO users (user_id, username, name, phone, selected_date, time_str) VALUES (?, ?, ?, ?, ?, ?)',
                        (user_id, name, name, phone, selected_date, time_str))
        
        # Фиксируем изменения
        conn.commit()
        


#table names
# hmi
# led
# tungsten
# kino_flo
# soft
# chimera
# stands_high
# power_distributors_and_cables
# lightning control
# grip
# tubes_trusses
# fog_hazer    
# other
# carts
# car_mount



# conn = sqlite3.connect('prosvet.db')
# cur = conn.cursor()

# cur.execute(''' INSERT INTO kino_flo (name, price) VALUES
# ('Светильник KINO FLO 4ft x 8lamps FLATHEAD', 1900),
# ('Светильник KINO FLO 4ft x 1lamps KIT', 600),
# ('Светильник KINO FLO 4ft x 4lamps KIT', 1200),
# ('Разноски бытовые 4ft ( одиночная лампа KINOFLO)', 150),
# ('Светильник KINO FLO 4ft x 2lamps KIT', 800),
# ('Разноски с балластом KINO FLO 4ft', 300),
# ('Светильник KINO FLO 2ft x 4lamps KIT', 1400),
# ('Лампа цветная PHILIPS', 200),
# ('Светильник KINO FLO 2ft x 2lamps KIT', 700),
# ('Лампа KINO FLO 2ft', 200),
# ('Светильник MINI FLO KIT 2шт', 1500),
# ('Лампа KINO FLO 4ft', 400),
# ('Светильник KINO FLO 2ft x 1lamps KIT', 500);''')

# conn.commit()
# conn.close()