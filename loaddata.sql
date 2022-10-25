CREATE TABLE "Users" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "first_name" varchar,
  "last_name" varchar,
  "email" varchar,
  "bio" varchar,
  "username" varchar,
  "password" varchar,
  "profile_image_url" varchar,
  "created_on" date,
  "active" bit
);


CREATE TABLE "DemotionQueue" (
  "action" varchar,
  "admin_id" INTEGER,
  "approver_one_id" INTEGER,
  FOREIGN KEY(`admin_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`approver_one_id`) REFERENCES `Users`(`id`),
  PRIMARY KEY (action, admin_id, approver_one_id)
);

=======
>>>>>>> main

DROP TABLE "DemotionQueue"
CREATE TABLE "DemotionQueue" (
  "action" varchar,
  "admin_id" INTEGER,
  "approver_one_id" INTEGER,
  FOREIGN KEY(`admin_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`approver_one_id`) REFERENCES `Users`(`id`),
  PRIMARY KEY (action, admin_id, approver_one_id)
);


CREATE TABLE "Subscriptions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "follower_id" INTEGER,
  "author_id" INTEGER,
  "created_on" date,
  FOREIGN KEY(`follower_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Posts" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "category_id" INTEGER,
  "title" varchar,
  "publication_date" date,
  "image_url" varchar,
  "content" varchar,
  "approved" bit,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Comments" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "author_id" INTEGER,
  "content" varchar,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Reactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar,
  "image_url" varchar
);

CREATE TABLE "PostReactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "reaction_id" INTEGER,
  "post_id" INTEGER,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`reaction_id`) REFERENCES `Reactions`(`id`),
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`)
);

CREATE TABLE "Tags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);

CREATE TABLE "PostTags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "tag_id" INTEGER,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`tag_id`) REFERENCES `Tags`(`id`)
);

CREATE TABLE "Categories" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);


INSERT INTO Categories ('label') VALUES ('Nature');
INSERT INTO Categories ('label') VALUES ('Coding');
INSERT INTO Categories ('label') VALUES ('Sports');
INSERT INTO Categories ('label') VALUES ('Lord Godzilla');

INSERT INTO Tags ('label') VALUES ('PYTHON');
INSERT INTO Tags ('label') VALUES ('JavaScript');
INSERT INTO Tags ('label') VALUES ('CSS');
INSERT INTO Tags ('label') VALUES ('HTML');
INSERT INTO Tags ('label') VALUES ('Unknown');

INSERT INTO Reactions ('label', 'image_url') VALUES ('happy', 'https://pngtree.com/so/happy');
INSERT INTO Reactions ('label', 'image_url') VALUES ('sad', 'https://pngtree.com/so/sad');
INSERT INTO Reactions ('label', 'image_url') VALUES ('indiff', 'https://pngtree.com/so/indifferent');

INSERT INTO Comments VALUES (Null, 1, 1, 'LizardButthole');
INSERT INTO Comments VALUES (Null, 2, 1, 'CatButthole');
INSERT INTO Comments VALUES (Null, 1, 2, 'DogButthole');
INSERT INTO Comments VALUES (Null, 2, 2, 'GodButthole');

INSERT INTO PostReactions VALUES (Null, 1, 1, 1);
INSERT INTO PostReactions VALUES (Null, 1, 1, 2);
INSERT INTO PostReactions VALUES (Null, 2, 2, 1);
INSERT INTO PostReactions VALUES (Null, 2, 2, 2);

INSERT INTO PostTags VALUES (Null, 1, 1 );
INSERT INTO PostTags VALUES (Null, 1, 2 );
INSERT INTO PostTags VALUES (Null, 2, 1 );
INSERT INTO PostTags VALUES (Null, 2, 2 );

INSERT INTO Posts VALUES (Null, 1, 1, 'CatButthole', CURRENT_TIMESTAMP, 'CatButtholePic.img', 'Meow', True);
INSERT INTO Posts VALUES (Null, 1, 2, 'DogButthole', CURRENT_TIMESTAMP, 'DogButtholePic.img', 'Bark', True);
INSERT INTO Posts VALUES (Null, 2, 1, 'GodButthole', CURRENT_TIMESTAMP, 'GodButtholePic.img', 'Thunder', False);
INSERT INTO Posts VALUES (Null, 2, 2, 'NoneButthole', CURRENT_TIMESTAMP, 'NoneButtholePic.img', 'Twerk', True);

INSERT INTO Subscriptions VALUES (Null, 1, 1, CURRENT_TIMESTAMP);
INSERT INTO Subscriptions VALUES (Null, 1, 2, CURRENT_TIMESTAMP);
INSERT INTO Subscriptions VALUES (Null, 2, 2, CURRENT_TIMESTAMP);
INSERT INTO Subscriptions VALUES (Null, 2, 1, CURRENT_TIMESTAMP);

INSERT INTO Users VALUES (NULL, 'matt', 'Martino', 'matt@email.com', 'Happenin Dude', 'MattCat', 'butthole', 'MattCat.img', CURRENT_TIMESTAMP, True);
INSERT INTO Users VALUES (NULL, 'Kelly', 'franidonno', 'kelly@email.com', 'Happenin lady', 'KellyCat', 'butthole', 'KellyCat.img', CURRENT_TIMESTAMP, True);
INSERT INTO Users VALUES (NULL, 'Nick', 'ClastName', 'Nick@email.com', 'Happenin Dude', 'NickCat', 'butthole', 'NickCat.img', CURRENT_TIMESTAMP, True);
INSERT INTO Users VALUES (NULL, 'Scott', 'Parks', 'Scott@email.com', 'Happenin Dude', 'ScottCat', 'butthole', 'scottCat.img', CURRENT_TIMESTAMP, True);

SELECT
    p.id,
    p.user_id,
    p.category_id,
    p.title,
    p.publication_date,
    p.image_url,
    p.content,
    p.approved
FROM Posts p

INSERT INTO Categories ('label') VALUES ('Nature');

SELECT
    p.id,
    p.user_id,
    p.category_id,
    p.title,
    p.publication_date,
    p.image_url,
    p.content,
    p.approved,
    c.label categorie_label
FROM Posts p
JOIN Categories c
    ON c.id = p.category_id


SELECT
    u.id,
    u.first_name,
    u.last_name,
    u.username,
    u.email,
    u.password,
    u.bio,
    u.profile_image_url,
    u.created_on,
    u.active
FROM Users u

SELECT
    u.id,
    u.first_name,
    u.last_name,
    u.username,
    u.email,
    u.password,
    u.bio,
    u.profile_image_url,
    u.created_on,
    u.active
FROM Users u
WHERE u.id = 2

SELECT
    p.id,
    p.user_id,
    p.category_id,
    p.title,
    p.publication_date,
    p.image_url,
    p.content,
    p.approved,
    c.label categorie_label
FROM Posts p
JOIN Categories c
    ON c.id = p.category_id

SELECT * FROM Tags
ORDER BY label ASC


SELECT
  t.id,
  t.label
FROM Tags t