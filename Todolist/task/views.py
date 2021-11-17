from flask import render_template
from flask_login import login_required
from .models import Category
from . import task
from .. import db

@task.route('/create-task')
@login_required
def tasks():
    categories= Category.query.all()
    return render_template('task/task.html', title='Create Tasks', categories=categories)
