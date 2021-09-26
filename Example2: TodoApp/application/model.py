from application import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)
    
    def __repr__(self):
        return f'<Todo ID: {self.id}, description: {self.description}>'