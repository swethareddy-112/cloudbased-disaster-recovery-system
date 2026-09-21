import sqlite3
import os

DATABASE = "data/database.db"


def create_database():

    os.makedirs("data", exist_ok=True)

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS backups (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            backup_time DATETIME DEFAULT CURRENT_TIMESTAMP,
            status TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def add_backup(filename, status):

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO backups (filename, status)
        VALUES (?, ?)
    """, (filename, status))

    connection.commit()
    connection.close()


def get_backups():

    connection = sqlite3.connect(DATABASE)

    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM backups
        ORDER BY id DESC
    """)

    data = cursor.fetchall()

    connection.close()

    return [dict(row) for row in data]