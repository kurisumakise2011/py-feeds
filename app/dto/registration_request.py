from app.exception.validation_exception import ValidationException


class RegistrationRequest(object):
    def __init__(self, login, name, password) -> None:
        super().__init__()
        self.login = login
        self.name = name
        self.password = password

    @staticmethod
    def from_json(data):
        if not data:
            raise ValidationException('Empty data')
        register = RegistrationRequest(data['username'], data['name'], data['password'])
        if register.password and register.login and register.name:
            return register
        else:
            raise ValidationException
