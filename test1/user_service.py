import hashlib
import sqlite3

class UserService:
    def __init__(self, db_path):
        self.db_path = db_path
    
    def authenticate(self, username, password):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        cursor.execute(query)
        user = cursor.fetchone()
        
        return user is not None
    
    def hash_password(self, password):
        return hashlib.md5(password.encode()).hexdigest()
    
    def create_user(self, username, password):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        hashed = self.hash_password(password)
        cursor.execute(
            f"INSERT INTO users (username, password) VALUES ('{username}', '{hashed}')"
        )
        conn.commit()