from aiohttp import ClientSession

from app.dto.article_dto import ArticleDto
from app.dto.search_request import SearchRequest


class HackerNewsSearcher:
    def __init__(self) -> None:
        super().__init__()

    async def search_news(self, search_request: SearchRequest):
        resp = await self._perform_request(search_request)
        hits = resp['hits']
        articles = []
        for hit in hits:
            articles.append(
                ArticleDto(title=hit['title'],
                           created_at=hit['created_at'],
                           url=hit['url'],
                           author=hit['author'],
                           story_text=hit['story_text'],
                           comment_text=hit['comment_text'],
                           points=hit['points'],
                           object_id=hit['objectID'],
                           index_keyword=search_request.keyword)
            )

        return articles

    async def _perform_request(self, search_request):
        async with ClientSession() as session:
            async with session.get(url='http://hn.algolia.com/api/v1/search?query='
                                       + search_request.keyword + "&tags=story") as resp:
                return await resp.json()
