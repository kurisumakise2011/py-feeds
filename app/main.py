import logging as log
import time

import aiohttp_cors
from aiohttp import web
from aiohttp_security import setup as setup_security, JWTIdentityPolicy

from app.controller.article_controller import ArticleController
from app.controller.auth_controller import AuthController
from app.controller.auth_filter import auth_middleware
from app.controller.auth_policy import PyFeedsAuthorizationPolicy
from app.controller.user_controller import UserController
from app.repository.article_repository import ArticleRepository
from app.repository.db_wrapper import Pool
from app.repository.user_repository import UserRepository
from app.service.article_service import ArticleService
from app.service.hacker_news_searcher import HackerNewsSearcher
from app.service.token_service import TokenService
from app.service.user_service import UserService
from app.util.config_utils import load_config


def init_app(config) -> web.Application:
    # db pool
    db_config = {
        'database': config['db']['database'],
        'user': config['db']['user'],
        'password': config['db']['password'],
        'host': config['db']['host'],
        'port': config['db']['port'],
    }
    time.sleep(5)
    pool = Pool(db_config)

    # components
    repos = {
        'article_repository': ArticleRepository(pool),
        'user_repository': UserRepository(pool)
    }

    # To make sure that we are connected to db
    repos['article_repository'].now()

    searcher = HackerNewsSearcher()
    services = {
        'user_service': UserService(repos['user_repository']),
        'hacker_news_searcher': searcher,
        'article_service': ArticleService(repos['article_repository'], searcher),
        'token_service': TokenService(config, repos['user_repository'])
    }

    controllers = {
        'auth_controller': AuthController(services['user_service'],
                                          services['token_service'],
                                          config['fe_redirect']),
        'article_controller': ArticleController(services['article_service']),
        'user_controller': UserController()
    }

    # web configuration
    app = web.Application(middlewares=[auth_middleware])
    app['config'] = config

    # setup routes
    app.add_routes([web.post('/users/authenticate', controllers['auth_controller'].auth),
                    web.post('/users/register', controllers['auth_controller'].signin),
                    web.get('/users/githubsso', controllers['auth_controller'].githubsso),
                    web.get('/articles', controllers['article_controller'].get_all),
                    web.post('/articles', controllers['article_controller'].find_article),
                    web.delete('/articles', controllers['article_controller'].remove_article_by_id)])
    # cors
    cors = aiohttp_cors.setup(app, defaults={
        '*': aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
        )
    })

    # Configure CORS on all routes.
    for route in list(app.router.routes()):
        cors.add(route)

    # security
    setup_security(app, JWTIdentityPolicy(secret=config['secret']),
                   PyFeedsAuthorizationPolicy(services['user_service']))

    return app


def main(config_path) -> None:
    config = load_config(config_path)
    log.basicConfig(level=log.INFO, filename='log/pyfeeds.log',
                    filemode='w', format='%(asctime)s: %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')
    log.getLogger().addHandler(log.StreamHandler())
    web.run_app(init_app(config))


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', help='Provide path to config file')
    args = parser.parse_args()

    if args.config:
        main(args.config)
    else:
        parser.print_help()
