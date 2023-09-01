from sqlalchemy.exc import IntegrityError
from databases.models import register
from exceptions.personal_exception import personal_exception


#
# Clase que funciona como orquestador para el acceso a los datos en la persistencia
#

class repository_register:
    def __init__(self, session):
        self.session = session

    def save(self, email, name):
        new_register = register(email=email, name=name)
        self.session.add(new_register)
        try:
            self.session.commit()
            return new_register.id
        except IntegrityError as Argument:
            print(Argument)
            self.session.rollback()
            raise personal_exception("", "Registro Duplicado", 409)

    def all(self):
        return self.session.query(register.id, register.email, register.name).all()

    def show(self, id):
        return self.session.query(register.id, register.email, register.name).filter(register.id == id).first()
