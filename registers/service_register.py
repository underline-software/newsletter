import os
from exceptions.PersonalException import ResponseApiException
from registers.repository_register import repository_register
from databases.database import Session


class service_register:
    repository = ""

    def __init__(self):
        session = Session()
        self.repository = repository_register(session)

    def store(self, email, name):
        try:
            return self.repository.save(email, name)
        except Exception as Argument:
            raise ResponseApiException(os.getenv("MESSAGE_3"), str(Argument.args[1]), 422)

    def getAll(self):
        try:
            result = self.repository.all()
            if len(result) > 0:
                return [{'id': row.id, 'email': row.email, 'name': row.name} for row in result]
        except Exception as Argument:
            raise ResponseApiException(os.getenv("MESSAGE_2"), str(Argument.args[1]), 500)

    def show(self, id):
        result = self.repository.show(id)
        if result is not None and len(result) > 0:
            return {'id': result[0], 'email': result[1], 'name': result[2]}
        else:
            raise ResponseApiException(os.getenv("MESSAGE_2"), os.getenv("NOT_FOUND"), 404)

    def update(self, id, name):
        return self.repository.update(id, name)

    def delete(self, id):
        return self.repository.delete(id)
