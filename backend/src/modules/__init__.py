from flask_restplus import Resource, Api
from .todo.rest_api import NAMESPACE as todo_ns

API = Api(doc='/doc/', prefix='/api')

API.add_namespace(todo_ns)