import sqlite3
import json
from models import Category
from models.post import Post
from models.users import Users



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
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved,
            c.label categorie_label,
            u.first_name,
            u.last_name,
            u.email,
            u.bio,
            u.username,
            u.password,
            u.profile_image_url,
            u.created_on,
            u.active
        FROM Posts p
        JOIN Categories c
            ON c.id = p.category_id
        JOIN Users u
            ON u.id = p.user_id
       
        """)

        # Initialize an empty list to hold all animal representations
        posts = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
    for row in dataset:

        # Create an animal instance from the current row
        post = Post(row['id'], row['user_id'], row['category_id'], row['title'],
                    row['publication_date'], row['image_url'], row['content'], row['approved'])
        user = Users(row["id"], row["first_name"], row["last_name"], row["username"], row["email"],
                     row["password"], row["bio"], row["profile_image_url"], row["created_on"], row["active"])

        category = Category(row['id'], row['categorie_label'])

        # Add the dictionary representation of the location to the animal
        post.category = category.__dict__
        post.user = user.__dict__

        posts.append(post.__dict__)

    return json.dumps(posts)


def get_single_post(id):
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved,
            c.label categorie_label,
            u.first_name,
            u.last_name,
            u.email,
            u.bio,
            u.username,
            u.password,
            u.profile_image_url,
            u.created_on,
            u.active
        FROM Posts p
        JOIN Categories c
            ON c.id = p.category_id
        JOIN Users u
            ON u.id = p.user_id
        WHERE p.id = ?
        """, (id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        post = Post(data['id'], data['user_id'], data['category_id'], data['title'],
                    data['publication_date'], data['image_url'], data['content'], data['approved'])
        user = Users(data["id"], data["first_name"], data["last_name"], data["username"], data["email"],
                     data["password"], data["bio"], data["profile_image_url"], data["created_on"], data["active"])

        category = Category(data['id'], data['categorie_label'])

        post.category = category.__dict__
        post.user = user.__dict__
        return json.dumps(post.__dict__)


def delete_post(id):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Posts
        WHERE id = ?
        """, (id, ))


def create_post(new_post):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Posts
            ( user_id, category_id, title, publication_date, image_url, content, approved )
        VALUES
            ( ?, ?, ?, ?, ?, ?, ?);
        """, (new_post['user_id'], new_post['category_id'], new_post['title'], new_post['publication_date'], new_post['image_url'], new_post['content'], new_post['approved'], ))

        id = db_cursor.lastrowid

        new_post['id'] = id

    return json.dumps(new_post)



def update_post(id, new_post):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Posts
            SET
                category_id = ?,
                title = ?,
                image_url = ?,
                content = ?
        WHERE id = ?
        """, (new_post['category_id'], new_post['title'], new_post['image_url'], new_post['content'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True