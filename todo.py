from baker import app, db
from baker.models import User, Todo

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Todo': Todo}

