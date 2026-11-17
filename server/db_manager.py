import sqlite3
import os
import hashlib


class DatabaseManager:
    def __init__(self, db_name="gonmigel.db"):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.join(current_dir, db_name)
        self.create_tables()

    def get_connection(self):
        return sqlite3.connect(self.db_path)

    def _hash_password(self, password):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

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

    def register_user(self, username, password, interests=None):
        if not username or not password:
            return False, "Username and password cannot be empty"

        password_hash = self._hash_password(password)
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
            return True, "Registration successful"
        except sqlite3.IntegrityError:
            return False, "Username already exists"
        finally:
            conn.close()

    def validate_login(self, username, password):
        if not username or not password:
            return False, "Username and password cannot be empty"

        password_hash = self._hash_password(password)
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute('''
            SELECT id FROM Users WHERE username = ? AND password_hash = ?
        ''', (username, password_hash))

        user = cursor.fetchone()
        conn.close()

        if user:
            return True, "Login successful"
        else:
            return False, "Invalid username or password"

    def get_user_interests(self, username):
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute('''
            SELECT Interests.interest_name 
            FROM Interests 
            JOIN Users ON Users.id = Interests.user_id 
            WHERE Users.username = ?
        ''', (username,))

        rows = cursor.fetchall()
        conn.close()
        return [row[0] for row in rows]