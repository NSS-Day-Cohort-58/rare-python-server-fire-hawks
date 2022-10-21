class Post():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, user_id, category_id, publication_date, title, image_url, content, approved):
        self.id = id
        self.user_id = user_id
        self.category_id = category_id
        self.category = None
        self.publication_date = publication_date
        self.title = title
        self.image_url = image_url
        self.content = content
        self.approved = approved
