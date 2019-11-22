from app.exception.validation_exception import ValidationException


class SearchRequest:
    """The representation of search request"""

    def __init__(self, keyword, type):
        self.keyword = keyword
        self.type = type

    @staticmethod
    def from_json(data):
        if not data:
            raise ValidationException('Empty data')
        search = SearchRequest(data['keyword'], data['type'])
        if search.keyword and search.type:
            return search
        else:
            raise ValidationException
