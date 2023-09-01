import re


#
# Clase que revisa los string y emails para evitar cadenas de caracteres no permitidas.
#
class validate:
    regex_email = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

    regex_sqlinjection = re.compile(r'[^a-zA-Z0-9\s]')

    def is_valid_email(self, email):
        if re.fullmatch(self.regex_email, email):
            return email
        else:
            return ""

    def sanitize_string(self, string):
        sanitized_string = re.sub(self.regex_sqlinjection, '', string)
        return sanitized_string
