import os
import sqlite3
from sqlite3 import Error
from config import ROOT_DIR

def create_connection():
    conn = None
    try:
        db_path = os.path.join(ROOT_DIR, 'data','user_management.db')
        isExist = os.path.exists(db_path)
        conn = sqlite3.connect(db_path)

        if not isExist:
            create_tables(conn)

        return conn
    except Error as e:
        #TODO: Handle error
        print(e)

def create_tables(conn):
    #TODO: Need to determine the tables fields
    try:
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            email TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )''')

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                price REAL NOT NULL
            )
        """)

        conn.commit()
    except Error as e:
        #TODO: Handle error
        print(e)