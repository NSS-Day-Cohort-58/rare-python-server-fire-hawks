import sqlite3
import json
from models import PostTags


def get_all_post_tags():
    # Open a connection to the database
    with sqlite3.connect("./db.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            g.id,
            g.post_id,
            g.tag_id
        FROM PostTags g
        """)

        post_tags = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            post_tag = PostTags(row['id'], row['post_id'], row['tag_id'])

            post_tags.append(post_tag.__dict__)

    return json.dumps(post_tags)


def get_single_post_tag(id):
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            g.id,
            g.post_id,
            g.tag_id
        FROM PostTags g
        WHERE g.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        post_tag = PostTags(data['id'], data['post_id'], data['tag_id'])

        return json.dumps(post_tag.__dict__)

def create_post_tag(new_post_tag):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO PostTags
            ( post_id, tag_id )
        VALUES
            ( ?, ? );
        """, (new_post_tag['post_id'], new_post_tag['tag_id'],))

        id = db_cursor.lastrowid

        new_post_tag['id'] = id
    return json.dumps(new_post_tag)

def delete_post_tag(id):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM PostTags
        WHERE id = ?
        """, (id, ))