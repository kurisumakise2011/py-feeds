import re

import jwt
from aiohttp.web_response import json_response
from jwt import DecodeError, ExpiredSignatureError

from app.domain.user import User
from app.exception.authorization_exception import AuthorizationException


async def auth_middleware(app, handler):
    async def middleware(request):
        if request.method == 'OPTIONS':
            return await handler(request)

        url = request.url.path
        whitelist = app['config']['whitelist']
        if re.match(whitelist, url):
            return await handler(request)

        request.user = None
        jwt_token = request.headers.get('Authorization', None)
        if jwt_token:
            try:
                payload = jwt.decode(jwt_token, app['config']['secret'])
            except (DecodeError, ExpiredSignatureError):
                return json_response({'message': 'Token is invalid'}, status=401)

            request.user = User(payload['user_id'], payload['username'],
                                payload['name'], None,
                                payload['created_at'])
            return await handler(request)
        else:
            raise AuthorizationException

    return middleware
