import json

from aiohttp.web_response import Response

from app.dto.credentials import Credentials
from app.dto.registration_request import RegistrationRequest
from app.exception.authorization_exception import AuthorizationException
from app.service.token_service import TokenService
from app.service.user_service import UserService


class AuthController(object):
    def __init__(self, user_service: UserService,
                 token_service: TokenService) -> None:
        super().__init__()
        self.user_service = user_service
        self.token_service = token_service

    async def auth(self, request) -> Response:
        post = await request.json()
        cred = Credentials.from_json(post)
        user = self.user_service.authorize(cred)
        if user:
            return Response(text=json.dumps({
                'username': user.username,
                'user_id': user.user_id,
                'name': user.name,
                'created_at': user.created_at,
                'token': self.token_service.generate_jwt(user)}
            ),
                status=200)
        else:
            raise AuthorizationException(message='Username or password is incorrect')

    async def signin(self, request) -> Response:
        post = await request.json()
        registration = RegistrationRequest.from_json(post)
        user_id = self.user_service.register(registration)

        return Response(text=json.dumps(self.user_service.find_user_by_id(user_id).__dict__),
                        status=201)

    async def githubsso(self, request) -> Response:
        print(request)
        return Response(text='')
