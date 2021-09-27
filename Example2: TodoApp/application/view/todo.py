from application import app, db
from flask import render_template, request, redirect, url_for, jsonify
from application.model import Todo
#optional import of sys lib
import sys

@app.route('/')
def index():
    todos = Todo.query.order_by('id').all()
    return render_template('index.html', data=todos)

@app.route('/todos/create', methods=['POST'])
def todos_create():
    error = False
    body = {}
    try:
        description = request.get_json()['description']
        todo = Todo(description=description)
        db.session.add(todo)
        db.session.commit()
        body['description'] = todo.description
    except:
        error = True #Setting error to true if there is an exception running application
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    if not error:
        return jsonify(body)

@app.route('/todos/<todo_id>/set-completed', methods=['POST'])
def set_complished_todo(todo_id):
    try:
        completed = request.get_json()['completed']
        todo = Todo.query.get(todo_id)
        todo.completed = completed
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()
    return redirect(url_for('index'))


@app.route('/todos/<todo_id>', methods=['DELETE'])
def delete_todos(todo_id):
    Todo.query.filter_by(id=todo_id).delete()
    db.session.commit()
    return jsonify({
        'Success' : True
    })