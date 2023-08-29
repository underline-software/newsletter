from databases.models import register

class repository_register:
    def __init__(self, session):
        self.session = session

    def save(self, email, name):
        newRegister = register(email=email, name=name)
        self.session.add(newRegister)
        self.session.commit()

    def all(self):
        return self.session.query(register.id, register.email, register.name).all()

    def show(self, id):
        return self.session.query(register.id, register.email, register.name).filter(register.id==id).first()

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
