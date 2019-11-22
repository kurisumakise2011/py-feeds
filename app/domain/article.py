class Article:
    def __init__(self, article_id, title, created_at,
                 comment_text, content, fetched_at, author,
                 url, index_keyword) -> None:
        self.article_id = article_id
        self.title = title
        self.created_at = created_at
        self.comment_text = comment_text
        self.content = content
        self.fetched_at = fetched_at
        self.author = author
        self.url = url
        self.index_keyword = index_keyword
