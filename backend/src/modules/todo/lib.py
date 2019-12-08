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
    # Delete set's key and subkeys.
    db_response = redis_con.srem(redis_key, todo_id)
    LOGGER.debug(f'Deleted from key: {redis_key} element: {todo_id}')
    redis_key = ":".join((redis_key, todo_id))
    db_response = redis_con.delete(redis_key)
    LOGGER.debug(f'Deleted hash element: {redis_key}')

    return db_response

def toggle_todo_status(todo_id):
    """ Change todos status. """
    redis_key = 'todos'
    todo_ids = redis_con.smembers(redis_key)
    # If no todos, return empty.
    if (not todo_ids or len(todo_ids) <= 0 or todo_id not in todo_ids):
        return None
    # Get current status.
    redis_key = ":".join((redis_key, todo_id))
    curr_status = redis_con.hget(redis_key, "status")
    # By default new status is undone.
    new_status = "undone"
    if (curr_status and curr_status != "done"):
        new_status = "done"
    redis_con.hset(redis_key, "status", new_status)
    LOGGER.debug(f'Update key: {redis_key} with status: {new_status}')

    return new_status

