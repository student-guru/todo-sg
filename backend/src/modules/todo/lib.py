""" Helper functions. """
from config import CONFIGURATION

LOGGER = CONFIGURATION.get_logger(__name__)
redis_con = CONFIGURATION.get_db()

def get_all_todos():
    """ Return all todos from database. """
    redis_key = 'todos'
    todo_nums = redis_con.smembers(redis_key)
    # If no todos, return empty.
    if (not todo_nums or len(todo_nums) <= 0):
        return None
    # Get all todos
    todos = []
    for todo_num in todo_nums:
        temp_key = ":".join((redis_key, todo_num))
        todo = redis_con.hgetall(temp_key)
        todos.append(todo)

    return todos
