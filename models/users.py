class Users:
    def __init__(
        self,
        id,
        firstName,
        lastName,
        userName,
        email,
        password,
        bio,
        profileImgUrl,
        active,
        created_on
    ):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.userName = userName
        self.email = email
        self.password = password
        self.bio = bio
        self.profileImgUrl = profileImgUrl
        self.created_on = created_on
        self.active = active
