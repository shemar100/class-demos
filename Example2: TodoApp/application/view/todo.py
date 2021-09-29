from application import app, db
from flask import render_template, request, redirect, url_for, jsonify
from application.model import Todo, TodoList
#optional import of sys lib
import sys

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
        'success' : True
    })


@app.route('/list/<list_id>')
def get_list_todos(list_id):
    list = TodoList.query.all()
    todos = Todo.query.filter_by(list_id=list_id).order_by('id').all()
    return render_template('index.html', todos=todos, list=list)

#redirects home route to get_list_todos route eg. list/num
@app.route('/')
def index():
    return redirect(url_for('get_list_todos', list_id=1))