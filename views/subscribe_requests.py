import sqlite3
import json
from models import Subscriptions


def get_all_subscriptions():
    # Open a connection to the database
    with sqlite3.connect("./db.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            u.id,
            u.follower_id,
            u.author_id,
            u.created_on
        FROM Subscriptions u
        """)

        subscriptions = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            subscription = Subscriptions(row['id'], row['follower_id'], row['author_id'], row['created_on'])

            subscriptions.append(subscription.__dict__)

    return json.dumps(subscriptions)


def get_single_subscription(id):
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            u.id,
            u.follower_id,
            u.author_id,
            u.created_on
        FROM Subscriptions u
        WHERE u.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        subscription = Subscriptions(data['id'], data['follower_id'], data['author_id'], data['created_on'])

        return json.dumps(subscription.__dict__)

def create_subscription(new_subscription):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Subscriptions
            ( follower_id, author_id, created_on )
        VALUES
            ( ?, ?, ? );
        """, (new_subscription['follower_id'], new_subscription['author_id'], new_subscription['created_on'], ))

        id = db_cursor.lastrowid

        new_subscription['id'] = id
    return json.dumps(new_subscription)

def delete_subscription(id):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Subscriptions
        WHERE id = ?
        """, (id, ))