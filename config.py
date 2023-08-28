import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())


class config:
    DEBUG = os.getenv("DEBUG")
    SERVER_NAME = os.getenv("CONTAINER_IP") + ":" + os.getenv("PORT")
