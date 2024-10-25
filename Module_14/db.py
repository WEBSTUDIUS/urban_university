import sqlite3


def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('database.db', 5)
        print(f'{sqlite3.version} connected to the SQLite database')
    except sqlite3.Error as e:
        print(e)

    return conn


def close_connection(conn):
    if conn:
        conn.close()
        print("Database connection closed")


def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )'''
                   )
    conn.commit()
    print("Table created successfully")


def drop_table(conn):
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS users')
    conn.commit()
    print("Table deleted successfully")


def create_index(conn, field):
    try:
        cursor = conn.cursor()
        cursor.execute(f'CREATE INDEX IF NOT EXISTS idx_{field} ON users(email)')
        conn.commit()
        print("Index created successfully")
    except sqlite3.Error as e:
        print(e)


def insert_user(conn, user):
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users(name, email, age, balance) VALUES(?,?,?,?)', user)
    conn.commit()
    print("User inserted successfully")


def get_user(conn, user_field, operator, value):
    cursor = conn.cursor()
    cursor.execute(f'SELECT name, email, age, balance FROM users WHERE {user_field}{operator}"{value}"')
    users = cursor.fetchall()
    if users is None:
        print("Users not found")
    return users


def update_user(conn, user, email):
    cursor = conn.cursor()
    cursor.execute(f'UPDATE users SET name=?, email=?, age=?, balance=? WHERE email="{email}"', user)
    conn.commit()
    print("User updated successfully")


def delete_user(conn, email):
    cursor = conn.cursor()
    cursor.execute(f'DELETE FROM users WHERE email=?', (email,))
    conn.commit()
    print("User deleted successfully")


connect = create_connection()

if connect is not None:
    drop_table(connect)
    create_table(connect)

    create_index(connect, 'email')

    for i in range(1, 11):
        user = (f'User{i}', f'user{i}@example.com', i * 10, 1000)
        insert_user(connect, user)

    for i in range(1, 11, 2):
        user = (f'User{i}', f'user{i}@example.com', i * 10, 500)
        update_user(connect, user, f'user{i}@example.com')

    for i in range(1, 11, 3):
        delete_user(connect, f'user{i}@example.com')

    for user in get_user(connect, 'age', '<>', 60):
        print(f'Name: {user[0]}, Email: {user[1]}, Age: {user[2]}, Balance: {user[3]}')

    # update_user(connect, ('John Doe','johndoe@example.com', 101), 'johndoe@example.com')
    # delete_user(connect, 'johndoe@example.com')

    close_connection(connect)
