from flask import jsonify

from exceptions.Error import Error


class ResponseApiException(Error):
    def __init__(self, message, error, code):
        self.message = message
        self.error = error
        self.code = code
