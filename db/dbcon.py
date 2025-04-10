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



categories = [
    'HMI',
    'LED',
    'TUNGSTEN',
    'KINO FLO',
    'SOFT',
    'CHIMERA',
    'STANDS HIGH ROLLER C-STAND',
    'POWER DISTRIBUTORS AND CABLES',
    'LIGHTING CONTROL',
    'GRIP',
    'TUBES TRUSSES',
    'FOG HAZER',
    'OTHER',
    'CARTS',
    'Car Mount'
]



conn = sqlite3.connect('prosvet.db')
cur = conn.cursor()

cur.execute('''
        CREATE TABLE IF NOT EXISTS hmi (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            availability INTEGER,
            amount INTGER, 
            price INTEGER 
        )
    ''')

cur.execute('''
        CREATE TABLE IF NOT EXISTS led (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            availability INTEGER,
            amount INTGER, 
            price INTEGER 
            
        )
    ''')

cur.execute('''
        CREATE TABLE IF NOT EXISTS tungsten (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            availability INTEGER,
            amount INTGER, 
            price INTEGER 
            
        )
    ''')

cur.execute('''
        CREATE TABLE IF NOT EXISTS tungsten (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            availability INTEGER,
            amount INTEGER,
            price INTEGER
            
        )
    ''')

cur.execute('''
        CREATE TABLE IF NOT EXISTS kino_flo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            availability INTEGER,
            amount INTEGER,
            price INTEGER
            
        )
    ''')

cur.execute('''
        CREATE TABLE IF NOT EXISTS soft (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            availability INTEGER,
            amount INTEGER,
            price INTEGER 
            
        )
    ''')

cur.execute('''
        CREATE TABLE IF NOT EXISTS chimera (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            availability INTEGER,
            amount INTEGER,
            price INTEGER
            
        )
    ''')

cur.execute('''
        CREATE TABLE IF NOT EXISTS stands_high (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            availability INTEGER,
            amount INTEGER, 
            price INTEGER
        )
    ''')

cur.execute('''
        CREATE TABLE IF NOT EXISTS power_distributors_and_cables (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            availability INTEGER,
            amount INTEGER, 
            price INTEGER
        )
    ''')

cur.execute('''
        CREATE TABLE IF NOT EXISTS lighting_control (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            availability INTEGER,
            amount INTEGER, 
            price INTEGER
        )
    ''')

cur.execute('''
        CREATE TABLE IF NOT EXISTS grip (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            availability INTEGER,
            amount INTEGER, 
            price INTEGER
        )
    ''')

cur.execute('''
        CREATE TABLE IF NOT EXISTS tubes_trusses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            availability INTEGER,
            amount INTEGER, 
            price INTEGER
        )
    ''')

cur.execute('''
        CREATE TABLE IF NOT EXISTS fog_hazer (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            availability INTEGER,
            amount INTEGER, 
            price INTEGER
        )
    ''')

cur.execute('''
        CREATE TABLE IF NOT EXISTS other (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            availability INTEGER,
            amount INTEGER, 
            price INTEGER
        )
    ''')

cur.execute('''
        CREATE TABLE IF NOT EXISTS carts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            availability INTEGER,
            amount INTEGER, 
            price INTEGER
        )
    ''')

cur.execute('''
        CREATE TABLE IF NOT EXISTS car_mount (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            availability INTEGER,
            amount INTEGER, 
            price INTEGER
        )
    ''')

conn.commit()
conn.close()


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