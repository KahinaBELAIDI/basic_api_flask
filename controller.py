
from db import connect_to_db


def insert_image(image_name, depth, default_row, resized_row):
    db = connect_to_db()
    cursor = db.cursor()
    statement = "INSERT INTO images(image_name, depth, default_row, resized_row) VALUES (?, ?, ?, ? )"
    cursor.execute(statement, [image_name, depth, default_row, resized_row])
    db.commit()
    return True


def get_by_id(id):
    db = connect_to_db()
    cursor = db.cursor()
    statement = "SELECT image_name, depth, default_row, resized_row FROM images WHERE id = ?"
    cursor.execute(statement, [id])
    return cursor.fetchone()


def delete_image(id):
    db = connect_to_db()
    cursor = db.cursor()
    statement = "DELETE FROM images WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True


def get_images():
    db = connect_to_db()
    cursor = db.cursor()
    query = "SELECT id, image_name, resized_row FROM games"
    cursor.execute(query)
    return cursor.fetchall()
