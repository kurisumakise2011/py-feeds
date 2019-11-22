from app.domain.article import Article
from app.repository.abstract_repository import AbstractRepository
from app.repository.db_wrapper import Pool
from app.util.map_utils import to_str
from app.util.map_utils import time_to_str


def map_many(cursor):
    articles = []
    rs = cursor.fetchall()
    for row in rs:
        (article_id, title, created_at, comment_text,
         content, fetched_at, author, url, index_keyword) = row
        articles.append(Article(article_id, to_str(title), time_to_str(created_at),
                                to_str(comment_text), to_str(content), time_to_str(fetched_at),
                                to_str(author), to_str(url), to_str(index_keyword)))
    return articles


def map_one(cursor):
    rs = cursor.fetchone()
    if rs:
        (article_id, title, created_at, comment_text,
         content, fetched_at, author, url, index_keyword) = rs
        return Article(article_id, to_str(title), time_to_str(created_at),
                       to_str(comment_text), to_str(content), time_to_str(fetched_at),
                       to_str(author), to_str(url), to_str(index_keyword))
    else:
        return None


class ArticleRepository(AbstractRepository):
    def __init__(self, pool: Pool) -> None:
        super().__init__(pool)

    def create_article(self, article: Article) -> int:
        return self.execute(
            """insert into articles(title, created_at, description, 
            content, fetched_at, author, url, index_keyword) 
            values (%s, %s, %s, %s, %s, %s, %s, %s)""",
            (article.title, article.created_at, article.comment_text,
             article.content, article.fetched_at, article.author,
             article.url, article.index_keyword))

    def find_users_articles(self, user_id: int, limit: int, offset: int):
        return self.query(
            """select a.* from articles a 
            join users_articles ua on a.article_id = ua.article_id 
            and ua.user_id = %s order by a.article_id desc limit %s offset %s""",
            (user_id, limit, offset), map_many)

    def find_article_by_id(self, article_id: int) -> Article:
        return self.query("""select * from articles where article_id = %s""",
                          (article_id,), map_one)

    def find_articles_by_title(self, title: str):
        return self.query("""select * from articles where title like %s""",
                          ('%' + title + '%',), map_many)

    def find_articles_by_index(self, keyword: str):
        return self.query("""select * from articles where index_keyword like %s""",
                          ('%' + keyword + '%',), map_many)

    def remove_article_by_id(self, article_id: int, user_id: int):
        self.execute("""delete from users_articles where article_id = %s and user_id = %s""",
                     (article_id, user_id))

    def link_article_and_user(self, user_id: int, article_id: int):
        self.execute("""insert into users_articles(user_id, article_id) values (%s, %s)""",
                     (user_id, article_id))
