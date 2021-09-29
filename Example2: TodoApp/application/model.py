from os import name

from sqlalchemy.sql.expression import false
from application import db

class Todo(db.Model):
    __tablename__ = 'todo'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)
    list_id = db.Column(db.Integer, db.ForeignKey("todolist.id"), nullable=False)

#This is the parent model
class TodoList(db.Model):
    __tablename__ = 'todolist'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    todos = db.relationship('Todo', backref='list', lazy=True)
    
    def __repr__(self):
        return f'<Todo ID: {self.id}, name: {self.name}>'