from aiohttp_security import AbstractAuthorizationPolicy


class PyFeedsAuthorizationPolicy(AbstractAuthorizationPolicy):
    def __init__(self, user_service) -> None:
        self.user_service = user_service
        super().__init__()

    async def authorized_userid(self, identity):
        pass

    async def permits(self, identity, permission, context=None):
        pass
