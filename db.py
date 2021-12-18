import sqlite3
DATABASE_NAME = "images.db"


def connect_to_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    print('*** Here in db file : create tables ***')
    tables = [
        """ CREATE TABLE IF NOT EXISTS images(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            image_name TEXT NOT NULL ,
            depths TEXT NOT NULL,
            default_row TEXT NOT NULL,
            resized_row TEXT NOT NULL
        )
        """
    ]
    db = connect_to_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)
