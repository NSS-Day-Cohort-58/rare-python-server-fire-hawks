class Users:
    def __init__(
        self,
        id,
        first_name,
        last_name,
        username,
        email,
        password,
        bio,
        profile_image_url,
        active,
        created_on
    ):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = password
        self.bio = bio
        self.profile_image_url = profile_image_url
        self.created_on = created_on
        self.active = active
