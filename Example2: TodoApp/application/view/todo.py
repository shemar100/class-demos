from application import app, db
from flask import render_template, request, redirect, url_for
from application.model import Todo


@app.route('/')
def index():
    todos = Todo.query.all()
    return render_template('index.html', data=todos)

@app.route('/todos/create', methods=['POST'])
def todos_create():
    description = request.form.get('description', '')
    todo = Todo(description=description)
    db.session.add(todo)
    db.session.commit()
    return redirect(url_for('index'))
