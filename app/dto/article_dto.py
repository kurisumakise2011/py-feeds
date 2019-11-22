from datetime import datetime

from app.domain.article import Article


class ArticleDto:
    def __init__(self, title, url, author, points,
                 story_text, comment_text, object_id, created_at,
                 index_keyword) -> None:
        self.title = title
        self.url = url
        self.author = author
        self.points = points
        self.story_text = story_text
        self.comment_text = comment_text
        self.object_id = object_id
        self.created_at = created_at
        self.index_keyword = index_keyword

    def to_model(self) -> Article:
        return Article(0,
                       self.title,
                       self._to_correct_timestamp(self.created_at),
                       self.comment_text,
                       self.story_text,
                       str(datetime.now()),
                       self.author,
                       self.url,
                       self.index_keyword)

    @staticmethod
    def _to_correct_timestamp(timestamp):
        return timestamp.split(".", 1)[0].replace('T', ' ')
