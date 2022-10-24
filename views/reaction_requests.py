import sqlite3
import json
from models import Reaction


def get_all_reactions():
    # Open a connection to the database
    with sqlite3.connect("./db.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            r.id,
            r.label,
            r.image_url
        FROM Reactions r
        """)

        reactions = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            reaction = Reaction(row['id'], row['label'], row['image_url'])

            reactions.append(reaction.__dict__)

    return json.dumps(reactions)


def get_single_reaction(id):
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            r.id,
            r.label,
            r.image_url
        FROM Reactions r
        WHERE r.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        reaction = Reaction(data['id'], data['label'], data['image_url'])

        return json.dumps(reaction.__dict__)

def create_reaction(new_reaction):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Reactions
            ( label, image_url )
        VALUES
            ( ?, ? );
        """, (new_reaction['label'], new_reaction['image_url'], ))

        id = db_cursor.lastrowid

        new_reaction['id'] = id
    return json.dumps(new_reaction)

def delete_reaction(id):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Reactions
        WHERE id = ?
        """, (id, ))