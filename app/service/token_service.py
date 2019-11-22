import jwt

from app.domain.user import User


class TokenService(object):
    def __init__(self, secret) -> None:
        super().__init__()
        self.secret = secret

    def generate_jwt(self, user: User) -> dict:
        return jwt.encode({
            'username': user.username,
            'user_id': user.user_id,
            'name': user.name,
            'created_at': user.created_at
        }, self.secret).decode()
