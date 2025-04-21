import sqlite3
from datetime import datetime


# conn = sqlite3.connect('prosvet.db')
# cur = conn.cursor()

# # cur.execute('''DROP TABLE users''')
# # conn.commit()
# # conn.close()

# '

conn = sqlite3.connect('prosvet.db')
cur = conn.cursor()

cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER UNIQUE,
            username TEXT,
            name TEXT,
            phone STR, 
            selected_date STR,
            time_str STR
        )
    ''')
conn.commit()
conn.close()

def get_all_user_id():
    conn = sqlite3.connect("prosvet.db")
    cursor = conn.cursor()
    cursor.execute("SELECT user_id FROM users")
    user_ids = cursor.fetchall()
    conn.close()

    return user_ids

def get_all_time_str():
    conn = sqlite3.connect("prosvet.db")
    cursor = conn.cursor()
    cursor.execute("SELECT time_str FROM users")
    rows = cursor.fetchall()
    conn.close()

    booked_times = []

    for row in rows:
        if row[0]:
            time_blocks = row[0].strip().split('\n') 
            for block in time_blocks:
                block = block.strip()
                if "с" in block and "до" in block:
                        date_part = block.split("с")[0].strip()
                        date_time_parts = block.split("с")[1].split("до")
                        if len(date_time_parts) == 2:
                            start_time = date_time_parts[0].strip()
                            end_time = date_time_parts[1].strip()
                            booked_times.append((date_part, start_time, end_time))
    print(booked_times)
    return booked_times


def is_time_booked(day: int, month: int, time: str) -> bool:
    conn = sqlite3.connect('prosvet.db')
    cur = conn.cursor()
    cur.execute("SELECT time_str FROM users")
    all_times = cur.fetchall()
    conn.close()

    target_date = f"{str(day).zfill(2)}.{str(month).zfill(2)}"

    # Обработка нестандартного времени 24:00
    if time.strip() == "24:00":
        time = "23:59"

    try:
        target_time = datetime.strptime(time.strip(), "%H:%M").time()
    except ValueError:
        print(f"⛔ Неверный формат времени: {time}")
        return False

    for (time_str,) in all_times:
        if not time_str:
            continue

        blocks = time_str.strip().split('\n')
        for block in blocks:
            if "с" in block and "до" in block:
                try:
                    date_part = block.split("с")[0].strip()
                    time_range = block.split("с")[1].strip()
                    start_time_str, end_time_str = time_range.split("до")

                    # Заменяем 24:00 на 23:59
                    if start_time_str.strip() == "24:00":
                        start_time_str = "23:59"
                    if end_time_str.strip() == "24:00":
                        end_time_str = "23:59"

                    start_time = datetime.strptime(start_time_str.strip(), "%H:%M").time()
                    end_time = datetime.strptime(end_time_str.strip(), "%H:%M").time()

                    if date_part == target_date:
                        if start_time <= target_time <= end_time:
                            return True
                except Exception as e:
                    print(f"Ошибка в блоке '{block}': {e}")
                    continue

    return False

def db_delete_booking(booking_id: int):
    conn = sqlite3.connect('prosvet.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (booking_id,))
    conn.commit()
    conn.close()

def db_add_booking(name: str, phone: str, selected_date: str, time_str: str):
    conn = sqlite3.connect('prosvet.db')
    cur = conn.cursor()
    cur.execute('''
        INSERT OR REPLACE INTO users (name, phone, selected_date, time_str)
        VALUES (?, ?, ?, ?)
    ''', (name, phone, selected_date, time_str))
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
    with sqlite3.connect('prosvet.db') as conn:
        cur = conn.cursor()

        cur.execute('SELECT user_id FROM users WHERE user_id = ?', (user_id,))
        user = cur.fetchone()
            
        if user:
            cur.execute('UPDATE users SET name = ?, phone = ?, selected_date = ?, time_str = ? WHERE user_id = ?',
                            (name, phone, selected_date, time_str, user_id))
        else:
            cur.execute('INSERT INTO users (user_id, name, phone, selected_date, time_str) VALUES (?, ?, ?, ?, ?)',
                        (user_id, name, phone, selected_date, time_str))
            
            conn.commit()
            conn.close()
        

def db_get_info():
        conn = sqlite3.connect('prosvet.db')
        cur = conn.cursor()

        cur.execute("SELECT * FROM users")
        info = cur.fetchall()
        conn.commit()
        conn.close()
        return info

def db_get_user_ids():
        conn = sqlite3.connect('prosvet.db')
        cur = conn.cursor()

        cur.execute("SELECT user_id FROM users")
        user_users_id = cur.fetchall()
        conn.commit()
        conn.close()
        return user_users_id


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