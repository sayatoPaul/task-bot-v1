import sqlite3

# Подключение (один раз)
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

def create_table():
    try:
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        task TEXT,
        done INTEGER DEFAULT 0
        )
        ''')
        conn.commit()
    except Exception as e:
        print(f'Something went wrong. Error: {e}')

def add_task(user_id, task):
    try:
        cursor.execute('INSERT INTO tasks (user_id, task) VALUES (?, ?)', (user_id, task))
        conn.commit()
    except Exception as e:
        print(f'Something went wrong. Error: {e}')

def show_list(user_id):
    try:
        cursor.execute('SELECT * FROM tasks WHERE user_id = ?', (user_id,))
        return cursor.fetchall()
    except Exception as e:
        print(f'Ошибка: {e}')
        return []

def check_task(check, real_num, user_id):
    try:
        cursor.execute(
            'UPDATE tasks SET done = ? WHERE id = ? AND user_id = ?',
            (check, real_num, user_id)
        )
        conn.commit()
    except Exception as e:
        print(f'Ошибка: {e}')

def develop_get():
    cursor.execute('SELECT * FROM tasks')
    return cursor.fetchall()

def delete_task(real_num, user_id):
    try:
        cursor.execute('DELETE FROM tasks WHERE id = ? AND user_id = ?', (real_num, user_id))
        conn.commit()
        return True # по желанию 
    except Exception as e:
        print(f'Ошибка: {e}')
        return False # по желанию