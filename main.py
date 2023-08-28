import os

from flask import Flask
from databases.database import engine
from databases.models import Base
from config import config
from news.routes import pathNews
from registers.route import pathRegister

app = Flask(__name__)
app.config.from_object(config)
app.register_blueprint(pathNews, url_prefix='/api/n')
app.register_blueprint(pathRegister, url_prefix='/api/r')
with app.app_context():
    Base.metadata.create_all(bind=engine)
if __name__ == '__main__':
    app.run()
#     Happy coding!
