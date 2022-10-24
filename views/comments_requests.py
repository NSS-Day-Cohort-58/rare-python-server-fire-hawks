import sqlite3
import json
from models.comment import Comment


def get_all_comments():
    # Open a connection to the database
    with sqlite3.connect("./db.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            x.id,
            x.post_id,
            x.author_id,
            x.content
        FROM Comments x
        """)

        categorys = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            category = Comment(row['id'], row['post_id'],
                               row['author_id'], row['content'])

            categorys.append(category.__dict__)

    return json.dumps(categorys)


def get_single_comment(id):
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            x.id,
            x.post_id,
            x.author_id,
            x.content
        FROM Comments x
        WHERE x.id = ?
        """, (id, ))

        data = db_cursor.fetchone()

        category = Comment(data['id'], data['post_id'],
                           data['author_id'], data['content'])

        return json.dumps(category.__dict__)


def create_comment(new_comment):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Comments
            ( post_id, author_id, content )
        VALUES
            ( ?, ?, ?);
        """, (new_comment['post_id'], new_comment['author_id'],
              new_comment['content'], ))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the animal dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_comment['id'] = id

    return json.dumps(new_comment)

def delete_comment(id):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Comments
        WHERE id = ?
        """, (id, ))
