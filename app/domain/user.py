class User:
    def __init__(self, user_id, username, name, token, created_at) -> None:
        self.user_id = user_id
        self.username = username
        self.name = name
        self.token = token
        self.created_at = created_at
