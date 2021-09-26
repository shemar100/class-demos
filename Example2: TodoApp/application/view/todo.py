from application import app, db
from flask import render_template, request, redirect, url_for, jsonify
from application.model import Todo
#optional import of sys lib
import sys

@app.route('/')
def index():
    todos = Todo.query.all()
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