from exceptions.error import Error


#
# Clase que personaliza las excepciones con los parametros que requiero
#
class personal_exception(Error):
    def __init__(self, message, error, code):
        self.message = message
        self.error = error
        self.code = code
