""" Todo rest api module. """

# Python Libs
import logging
from flask_restplus import Resource, Namespace, reqparse
from flask import (request, jsonify)

# Project Files
from . import lib
from config import CONFIGURATION
from src.models.todo.todo import Todo as Todo_Model

NAMESPACE = Namespace(
    'todo', description='Api namespace representing a todo task.')

todo_model = NAMESPACE.parser()
todo_model.add_argument('status', type=str, default='done',
                        help='Status of the todo.', choices=['done', 'undone'] )
todo_model.add_argument('title', type=str, help='Title of the todo.')


@NAMESPACE.route('/')
class Todo(Resource):
    """
    Main api class for todo.
    """
    @NAMESPACE.expect(todo_model)
    def post(self):
        """ Add a todo to db. """
        # Parse args.
        args = request.args
        todo_status = args.get('status', '')
        todo_title = args.get('title', '')
        # Create todo.
        new_todo = Todo_Model(title=todo_title, status=todo_status)
        todo_dict = new_todo.save_to_db()
        # Response from server.
        response = todo_dict
        return jsonify(response)

@NAMESPACE.route('/<int:todo_id>')
class Todo(Resource):
    """
    Api class for specific todo.
    """
    def delete(self, todo_id):
        """ REmoves a todo from db. """
        todo_id = str(todo_id)
        # Response from server.
        response = lib.delete_todo(todo_id)
        if not response:
            response = "Key not found"
        else:
            response = "OK"
        return jsonify(response)

    def patch(self, todo_id):
        """ Change todo's status. """

        return "test"


@NAMESPACE.route('/all')
class Todos(Resource):
    """
    Main api class for all todos.
    """
    def get(self):
        """ Get all todos. """
        todos = lib.get_all_todos()
        # Response from server.
        response = todos
        return jsonify(response) 
