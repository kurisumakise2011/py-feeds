from app.domain.user import User
from app.dto.registration_request import RegistrationRequest
from app.repository.abstract_repository import AbstractRepository
from app.repository.db_wrapper import Pool
from app.util.map_utils import to_str
from app.util.map_utils import time_to_str


def map_one(cursor):
    rs = cursor.fetchone()
    if rs:
        (user_id, login, name, token, created_at) = rs
        return User(user_id, to_str(login), to_str(name), to_str(token), time_to_str(created_at))
    else:
        return None


def map_bool(cursor):
    rs = cursor.fetchone()
    if rs:
        return int(rs[0]) == 1
    else:
        return False


class UserRepository(AbstractRepository):
    def __init__(self, pool: Pool) -> None:
        super().__init__(pool)

    def find_user_by_login(self, login) -> User:
        return self.query("""select * from users where login = %s""", (login,), map_one)

    def find_user_by_id(self, user_id) -> User:
        return self.query("""select * from users where user_id = %s""", (user_id,), map_one)

    def create_new_user(self, request: RegistrationRequest) -> int:
        return self.execute("""insert into users(login, name, token) 
                             values (%s, %s, %s)""",
                            (request.login, request.name, request.password))

    def check_if_login_exists(self, login: str) -> bool:
        return self.query("""select exists (select 1 from users where login = %s)""",
                          (login,), map_bool)
