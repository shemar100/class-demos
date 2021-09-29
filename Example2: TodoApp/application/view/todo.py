from os import abort
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
        list_id = request.get_json()['list_id']
        todo = Todo(description=description, completed=False, list_id=list_id)
        db.session.add(todo)
        db.session.commit()
        body['id'] = todo.id
        body['complete'] = todo.completed
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

#redirects home route to get_list_todos route eg. list/num
@app.route('/')
def index():
    return redirect(url_for('get_list_todos', list_id=1))

@app.route('/lists/<list_id>')
def get_list_todos(list_id):
    lists = TodoList.query.all()
    todos = Todo.query.filter_by(list_id=list_id).order_by('id').all()
    active_list = TodoList.query.get(list_id) #based on the list_id returns the current list route to view
    return render_template('index.html', todos=todos, lists=lists, active_list=active_list)

@app.route('/lists/create', methods=['POST'])
def create_list():
    error = False
    body = {}
    try:
        name = request.get_json()['name']
        todoList = TodoList(name=name)
        db.session.add(todoList)
        db.session.commit()
        body['id'] = todoList.id
        body['name'] = todoList.name
    except:
        db.session.rollback()
        error = True
    finally:
        db.session.close()
    if error:
        abort(500)
    else:
        return jsonify(body)