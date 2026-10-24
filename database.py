import sqlite3
import os


class DatabaseManager:
    def __init__(self, db_name="gonmigel.db"):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.join(current_dir, db_name)
        self.create_tables()

    def get_connection(self):
        return sqlite3.connect(self.db_path)

    def create_tables(self):
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Interests (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                interest_name TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES Users (id) ON DELETE CASCADE
            )
        ''')

        conn.commit()
        conn.close()

    def add_user(self, username, password_hash, interests=None):
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('''
                INSERT INTO Users (username, password_hash)
                VALUES (?, ?)
            ''', (username, password_hash))

            user_id = cursor.lastrowid

            if interests:
                for interest in interests:
                    cursor.execute('''
                        INSERT INTO Interests (user_id, interest_name)
                        VALUES (?, ?)
                    ''', (user_id, interest))

            conn.commit()
            return user_id
        except sqlite3.IntegrityError:
            return None
        finally:
            conn.close()

    def get_user_by_username(self, username):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT id, username, password_hash FROM Users WHERE username = ?
        ''', (username,))
        user = cursor.fetchone()
        conn.close()
        return user

    def get_user_interests(self, user_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT interest_name FROM Interests WHERE user_id = ?
        ''', (user_id,))
        rows = cursor.fetchall()
        conn.close()
        return [row[0] for row in rows]


if __name__ == "__main__":
    db = DatabaseManager()