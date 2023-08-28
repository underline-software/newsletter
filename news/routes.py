from flask import Blueprint, jsonify
from externals.apis.news import news

pathNews = Blueprint('news', __name__)

@pathNews.route("/news", methods=["GET"])
def gets_news():
    try:
        api = news()
        return jsonify(api.get_externals_news()), 200
    except Exception as Argument:
        return jsonify({"message": str(Argument.args[0]), 'error': str(Argument.args[1])
                           , 'code': Argument.args[2]}), Argument.args[2]
