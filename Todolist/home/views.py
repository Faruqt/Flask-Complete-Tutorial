from flask import render_template
from flask_login import login_required
from ..models import Todo
from ..task.models import Category
from . import home
from .. import db

@home.route('/home')
@login_required
def homepage():
    todo= Todo.query.all()
    return render_template('home/home.html', title='Home Page', todo=todo)
