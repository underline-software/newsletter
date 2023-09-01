from flask import Blueprint, jsonify
from news.news_service import news_service as news

pathNews = Blueprint('news', __name__)


#
# Manejador de rutas para las noticias.
#

@pathNews.route("/news", methods=["GET"])
def gets_news():
    try:
        source = news()
        return jsonify(source.get_news()), 200, {'Access-Control-Allow-Origin': 'https://teguio.cl'}
    except Exception as Argument:
        return jsonify({"message": str(Argument.args[0]), 'error': str(Argument.args[1])
                           , 'code': Argument.args[2]}), Argument.args[2], {'Access-Control-Allow-Origin': 'https://teguio.cl'}
