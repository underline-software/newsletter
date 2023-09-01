import os
import requests
from exceptions.personal_exception import personal_exception
from dotenv import load_dotenv
load_dotenv()

#
# Clase que funciona como proveedor externo de servicio de noticias
#
class news:
    api_key = ""
    base_url = ""

    def __init__(self):
        self.api_key = os.getenv("NEWS-API-KEY")
        self.base_url = os.getenv("NEWS-API-URL")

    def get_externals_news(self):
        url = f"{self.base_url}{self.api_key}"
        try:
            response = requests.get(url, timeout=3)
            data = response.json()
            if response.status_code == 200:
                return data.get('articles', [])
            else:
                raise personal_exception(os.getenv("MESSAGE_1"), str(response.text), response.status_code)
        except Exception as Argument:
            raise personal_exception(os.getenv("MESSAGE_1"), str(Argument.args[1]), 500)
