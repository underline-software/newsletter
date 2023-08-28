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
        return self.repository.all()

    def show(self, id):
        return self.repository.show(id)

    def update(self, id, name):
        return self.repository.update(id, name)

    def delete(self, id):
        return self.repository.delete(id)
