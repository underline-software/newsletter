import os
from exceptions.personal_exception import personal_exception
from registers.repository_register import repository_register
from databases.database import Session
from cryptography.fernet import Fernet


#
# Clase que funciona como manejador de las reglas de negocio para el registro de newsletter
#

class service_register:
    repository = ""

    def __init__(self):
        session = Session()
        self.repository = repository_register(session)

    def store(self, email, name):
        try:
            if len(email) > 0 and len(name) > 0:
                cipher_suite = Fernet(os.getenv("SECRET_KEY"))
                return self.repository.save(cipher_suite.encrypt(email.encode('utf-8')), name)
            else:
                raise personal_exception("Campos vacios", "Largo de campos insuficiente", 400)
        except Exception as Argument:
            raise personal_exception(os.getenv("MESSAGE_3"), str(Argument.args[1]), str(Argument.args[2]))

    def all(self):
        try:
            result = self.repository.all()
            if len(result) > 0:
                cipher_suite = Fernet(os.getenv("SECRET_KEY"))
                return [{'id': row.id, 'email': cipher_suite.decrypt(row.email).decode('utf-8'), 'name': row.name} for row in result]
        except Exception as Argument:
            raise personal_exception(os.getenv("MESSAGE_2"), str(Argument.args[1]), 500)

    def show(self, id):
        result = self.repository.show(id)
        if result is not None and len(result) > 0:
            cipher_suite = Fernet(os.getenv("SECRET_KEY"))
            return {'id': result[0], 'email': cipher_suite.decrypt(result[1]).decode('utf-8'), 'name': result[2]}
        else:
            raise personal_exception(os.getenv("MESSAGE_2"), os.getenv("NOT_FOUND"), 404)
