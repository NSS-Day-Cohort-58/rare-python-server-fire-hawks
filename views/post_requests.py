import sqlite3
import json

from models.post import Post


def get_all_posts():
    # Open a connection to the database
    with sqlite3.connect("./db.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved
        FROM Posts p
       
        """)

        # Initialize an empty list to hold all animal representations
        posts = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
    for row in dataset:

        # Create an animal instance from the current row
        post = Post(row['id'], row['user_id'], row['category_id'],
                    row['publication_date'], row['image_url'], row['content'], row['approved'])

        posts.append(post.__dict__)

    return json.dumps(posts)


# def get_single_animal(id):
#     with sqlite3.connect("./kennel.sqlite3") as conn:
#         conn.row_factory = sqlite3.Row
#         db_cursor = conn.cursor()

#         # Use a ? parameter to inject a variable's value
#         # into the SQL statement.
#         db_cursor.execute("""
#         SELECT
#             a.id,
#             a.name,
#             a.breed,
#             a.status,
#             a.location_id,
#             a.customer_id
#         FROM animal a
#         WHERE a.id = ?
#         """, (id, ))

#         # Load the single result into memory
#         data = db_cursor.fetchone()

#         # Create an animal instance from the current row
#         animal = Animal(data['id'], data['name'], data['breed'],
#                         data['status'], data['location_id'],
#                         data['customer_id'])

#         return animal.__dict__
