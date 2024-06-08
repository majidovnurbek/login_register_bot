import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('pupil.db')
cursor = conn.cursor()
# Define the users table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username varchar(255),
        password VARCHAR(255),
    )
''')
conn.commit()


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def user_exists(self, password):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM 'users' WHERE 'password' = ?", (password,)).fetchmany(1)
            return bool(len(result))

    def add_user(self, username, password):
        with self.connection:
            return self.cursor.execute('INSERT INTO users (full_name, username, password) VALUES (?, ?, ?)',
                                       (username, password))
