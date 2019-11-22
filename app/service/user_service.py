from app.dto.credentials import Credentials
from app.domain.user import User
from app.dto.registration_request import RegistrationRequest
from app.exception.app_logic_exception import AppLogicException
from app.repository.user_repository import UserRepository
from app.util import security_utils


class UserService:
    def __init__(self, user_repo: UserRepository) -> None:
        super().__init__()
        self.user_repo = user_repo

    def authorize(self, cred: Credentials) -> User or None:
        user = self.user_repo.find_user_by_login(cred.username)
        if user:
            if security_utils.check_password_hash(cred.password, user.token):
                return user
            else:
                return None
        else:
            return None

    def register(self, request: RegistrationRequest) -> int:
        existing = self.user_repo.check_if_login_exists(request.login)
        if existing:
            raise AppLogicException(message='Such login already existing ' + request.login)
        token = security_utils.generate_password_hash(request.password)
        request.password = token
        return self.user_repo.create_new_user(request)

    def user_exits(self, login: str) -> bool:
        return self.user_repo.check_if_login_exists(login)

    def find_user_by_id(self, user_id: int) -> User:
        return self.user_repo.find_user_by_id(user_id)
