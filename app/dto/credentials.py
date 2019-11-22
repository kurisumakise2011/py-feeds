from app.exception.validation_exception import ValidationException


class Credentials:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    @staticmethod
    def from_json(data):
        if not data:
            raise ValidationException('Empty data')
        cred = Credentials(data['username'], data['password'])
        if cred.password and cred.username:
            return cred
        else:
            raise ValidationException
