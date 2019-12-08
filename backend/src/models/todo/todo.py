""" Module containing Todo classes. """
# Python libs.
import redis
# Project files.
from src import BCRYPT
from config import CONFIGURATION

redis_con = CONFIGURATION.get_db()
LOGGER = CONFIGURATION.get_logger(__name__)

class Todo():
    """ Class representing an App User. """
    def __init__(self, title, status):
        """ Class constructor """
        self.title = title
        self.status = status if (status and status != "") else "done"

    def save_to_db(self):
        """ Save the todo to db. """
        # Save todos under todos set.
        redis_key = 'todos'
        todos = redis_con.smembers(redis_key)
        # Check how many todos exist and create the next one.
        todos = list(todos)
        if todos:
            todos_number = 1 + len(todos)
        else:
            todos_number = 1

        redis_con.sadd(redis_key, str(todos_number))
        LOGGER.debug(f'Save to key: {redis_key} : {todos_number}')
        redis_key = ":".join((redis_key, str(todos_number)))
        todo_dict = {
                        'title': self.title,
                        'status': self.status
                     }
        redis_con.hmset(
            redis_key, todo_dict)
        LOGGER.debug(f'Save to key: {redis_key} : {todo_dict}')
