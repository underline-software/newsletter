from registers.repository_register import repository_register
from databases.database import Session


class service_register:
    repository = ""

    def __init__(self):
        session = Session()
        self.repository = repository_register(session)

    def store(self, email, name):
        return self.repository.save(email, name)

    def getAll(self):
        result = self.repository.all()
        if len(result) > 0:
            return [{'id': row.id, 'email': row.email, 'name': row.name} for row in result]

    def show(self, id):
        result = self.repository.show(id)
        if len(result) > 0:
            return {'id': result[0], 'email': result[1], 'name': result[2]}

    def update(self, id, name):
        return self.repository.update(id, name)

    def delete(self, id):
        return self.repository.delete(id)
