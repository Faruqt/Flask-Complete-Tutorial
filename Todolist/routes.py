from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required
from Todolist import app, db
from .models import Todo

@app.route('/')
def index():
    todo= Todo.query.all()
    return render_template('index.html', title='ToDo Application')



