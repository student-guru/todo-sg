""" Helper functions. """
from config import CONFIGURATION

LOGGER = CONFIGURATION.get_logger(__name__)
redis_con = CONFIGURATION.get_db()

def get_all_todos():
    """ Return all todos from database. """
    redis_key = 'todos'
    todo_ids = redis_con.smembers(redis_key)
    # If no todos, return empty.
    if (not todo_ids or len(todo_ids) <= 0):
        return None
    # Get all todos
    todos = []
    for todo_id in todo_ids:
        temp_key = ":".join((redis_key, todo_id))
        todo = redis_con.hgetall(temp_key)
        todo['id'] = todo_id
        todos.append(todo)

    return todos

def delete_todo(todo_id):
    """ Remove Todo from db """
    redis_key = 'todos'
    todo_ids = redis_con.smembers(redis_key)
    # If no todos, return empty.
    if (not todo_ids or len(todo_ids) <= 0 or todo_id not in todo_ids):
        return None
    db_response = redis_con.srem(redis_key, todo_id)
    LOGGER.debug(f'Deleted from key: {redis_key} element: {todo_id}')
    redis_key = ":".join((redis_key, todo_id))
    db_response = redis_con.delete(redis_key)
    LOGGER.debug(f'Deleted hash element: {redis_key}')

    return db_response


