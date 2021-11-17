from Todolist import app, db
from Todolist.models import Todo
from Todolist.auth.models import User

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Todo': Todo}

