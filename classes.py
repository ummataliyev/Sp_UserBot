import sqlite3

class UserInfo:
    def __init__(self, db: sqlite3):
        self.db = db
    
    def save_user_info(self, user_id, first_name, last_name=None, username=None, is_premium=None):
        conn = sqlite3.connect("/home/umidjon/Desktop/self/userbot/info.db")
        c = conn.cursor()
        c.execute(
            """
            INSERT INTO user_info (user_id, first_name, last_name, username, is_premium)
            VALUES (?, ?, ?, ?, ?)
            """,
            (user_id, first_name, last_name, username, is_premium)
        )
        conn.commit()
        conn.close()


sqlite3_client = UserInfo(sqlite3)
