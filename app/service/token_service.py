import logging as log

import jwt
from aiohttp import ClientSession

from app.domain.user import User
from app.dto.registration_request import RegistrationRequest
from app.repository.user_repository import UserRepository


class TokenService(object):
    def __init__(self, config,
                 user_repo: UserRepository) -> None:
        super().__init__()
        self.secret = config['secret']
        self.client_id = config['clientID']
        self.client_secret = config['client_secret']
        self.githubsso = config['githubsso']
        self.redirect_uri = config['github_redirect']
        self.user_url = config['github_user_url']
        self.fe_redirect = config['fe_redirect']
        self.user_repo = user_repo

    def generate_jwt(self, user: User) -> dict:
        return jwt.encode({
            'username': user.username,
            'user_id': user.user_id,
            'name': user.name,
            'created_at': user.created_at
        }, self.secret).decode()

    async def perform_github_authorization(self, code):
        async with ClientSession() as session:
            response = await self._perform_github_exchanging(
                session, {
                    "client_id": self.client_id,
                    "client_secret": self.client_secret,
                    "code": code,
                    "redirect_uri": self.redirect_uri
                })
            log.info("Got response from github %s", str(response))
            access_token = response['access_token']

            user = await self._get_github_user(session, access_token)
            user = await self._persist_user_to_db(user, access_token)
            return user

    async def _perform_github_exchanging(self, session, data):
        async with session.post(url=self.githubsso, data=data, headers={'Accept': ' application/json'}) as response:
            return await response.json()

    async def _get_github_user(self, session, token):
        async with session.get(url=self.user_url,
                               headers={'Accept': ' application/json',
                                        'Authorization': 'token ' + token}) as response:
            return await response.json()

    async def _persist_user_to_db(self, user, token):
        existing = self.user_repo.check_if_login_exists(user['login'])
        if existing:
            return self.user_repo.find_user_by_login(user['login'])
        else:
            user_id = self.user_repo.create_new_user(RegistrationRequest(user['login'], '', token))
            return self.user_repo.find_user_by_id(user_id)
