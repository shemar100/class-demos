from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Hotskull!000@localhost:5432/todoapp'
db = SQLAlchemy(app)

import application.view.todo

db.create_all()