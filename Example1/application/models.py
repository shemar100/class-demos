from application import db

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    #Helps in debug to represent object
    def __repr__(self):
        return f'<Person ID: {self.id}, name: {self.name}'