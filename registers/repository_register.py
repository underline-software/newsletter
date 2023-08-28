from databases.models import register
from sqlalchemy.orm import sessionmaker


class repository_register:
    def __init__(self, session):
        self.session = session

    def save(self, email, name):
        newRegister = register(email, name)
        self.session.add(newRegister)
        self.session.commit()

    def all(self):
        return self.session.query(register).all()

    def show(self, id):
        return self.session.query(register).filter_by(id=id).first()

    def update(self, id, name):
        updateRegister = self.show(id)
        if updateRegister:
            updateRegister.name = name
            self.session.commit()

    def delete(self, id):
        deleteRegister = self.show(id)
        if deleteRegister:
            self.session.delete(deleteRegister)
            self.session.commit()
