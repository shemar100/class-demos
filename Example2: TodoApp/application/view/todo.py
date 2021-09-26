from application import app, db
from flask import render_template, request, redirect, url_for, jsonify
from application.model import Todo


@app.route('/')
def index():
    todos = Todo.query.all()
    return render_template('index.html', data=todos)

@app.route('/todos/create', methods=['POST'])
def todos_create():
    description = request.get_json()['description']
    todo = Todo(description=description)
    db.session.add(todo)
    db.session.commit()
    return jsonify({
        'description' : todo.description
    })
