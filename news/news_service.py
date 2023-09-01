from externals.apis.news import news as api
#
# Clase que funciona como manejador de las reglas de negocio para las noticias
#

class news_service:
    def __init__(self, ):
        self.external_source = api()

    def get_news(self):
        news = self.external_source.get_externals_news()
        return news