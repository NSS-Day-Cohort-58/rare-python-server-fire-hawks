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
    ):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.userName = userName
        self.email = email
        self.password = password
        self.bio = bio
        self.profileImgUrl = profileImgUrl
        self.active = active
