from externals.apis.news import news as api


class news_service:
    def __init__(self, ):
        self.source = api()

    def get_news(self):
        news = self.source.get_externals_news()
        return news