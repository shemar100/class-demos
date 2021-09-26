from application import app
from flask import render_template
from application.model import Todo


@app.route('/')
def index():
    todos = Todo.query.all()
    return render_template('index.html', data=todos)