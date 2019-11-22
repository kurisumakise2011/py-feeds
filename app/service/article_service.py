from app.domain.article import Article
from app.dto.article_dto import ArticleDto
from app.dto.search_request import SearchRequest
from app.repository.article_repository import ArticleRepository
from app.service.hacker_news_searcher import HackerNewsSearcher


class ArticleService(object):
    def __init__(self, article_repo: ArticleRepository,
                 hacker_news_searcher: HackerNewsSearcher) -> None:
        super().__init__()
        self.article_repo = article_repo
        self.hacker_news_searcher = hacker_news_searcher

    def get_user_articles(self, user_id, limit=5, offset=1):
        return self.article_repo.find_users_articles(user_id, limit, offset)

    async def search_articles(self, user_id, search_request: SearchRequest):
        articles = await self.hacker_news_searcher.search_news(search_request)
        articles = [self._convert_article(article) for article in articles]
        [self._persist_article(article, user_id) for article in articles]
        return articles

    def _convert_article(self, article: ArticleDto) -> Article:
        return article.to_model()

    def _persist_article(self, article: Article, user_id: int):
        id = self.article_repo.create_article(article)
        self.article_repo.link_article_and_user(user_id, id)

    def remove_article_by_id(self, article_id, user_id):
        return self.article_repo.remove_article_by_id(article_id, user_id)
