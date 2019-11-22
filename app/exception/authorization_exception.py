import json

from aiohttp import web


class AuthorizationException(web.HTTPError):
    error = 'Not authorized'
    status_code = 401

    def __init__(self, message=None, status_code=None, **kwargs):

        if status_code is not None:
            self.status_code = status_code

        super().__init__(reason=message)
        if not message:
            message = self.error

        msg_dict = {'error': message}

        if kwargs:
            msg_dict['error_details'] = kwargs

        self.text = json.dumps(msg_dict)
        self.content_type = 'application/json'
