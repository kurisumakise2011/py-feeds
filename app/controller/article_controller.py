import json

from aiohttp.web_response import Response

from app.dto.search_request import SearchRequest
from app.service.article_service import ArticleService


class ArticleController:
    def __init__(self, article_service: ArticleService) -> None:
        super().__init__()
        self.article_service = article_service

    async def get_all(self, request) -> Response:
        rel_url = request.rel_url
        user = request.user
        limit = int(rel_url.query['limit'])
        offset = int(rel_url.query['offset'])

        articles = self.article_service.get_user_articles(user.user_id,
                                                          limit,
                                                          offset)
        articles = json.dumps([article.__dict__ for article in articles])
        return Response(status=200, text=articles)

    async def find_article(self, request) -> Response:
        data = await request.json()
        search = SearchRequest.from_json(data)
        articles = await self.article_service.search_articles(request.user.user_id, search)
        articles = json.dumps([article.__dict__ for article in articles])
        return Response(status=201, text=articles)

    async def remove_article_by_id(self, request) -> Response:
        to_delete = request.rel_url.query['article_id']
        user = request.user
        self.article_service.remove_article_by_id(to_delete, user)
        return Response(status=204)
