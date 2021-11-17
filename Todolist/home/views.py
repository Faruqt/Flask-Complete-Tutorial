from flask import render_template
from flask_login import login_required, current_user
from ..models import Todo
from ..task.models import Category
from . import home
from datetime import datetime

@home.route('/home')
@login_required
def homepage():
    user = current_user
    todo= Todo.query.filter_by(author=user)
    date= datetime.now()
    now= date.strftime("%Y-%m-%d")

    category1 = Category.query.get(1) 
    category2 = Category.query.get(2) 
    category3 = Category.query.get(3) 

    Task_ID_Business = Todo.query.filter_by(category= "Business", author=user) 
    Task_ID_Personal = Todo.query.filter_by(category= "Personal", author=user)
    Task_ID_Other = Todo.query.filter_by(category= "Other", author=user)

    no_of_Task_ID_Business=Task_ID_Business.count()
    no_of_Task_ID_Personal=Task_ID_Personal.count()
    no_of_Task_ID_Other=Task_ID_Other.count()

    return render_template('home/home.html', title='Home Page',
                            todo=todo, no_of_business_tasks=no_of_Task_ID_Business, 
                            no_of_other_tasks= no_of_Task_ID_Other, 
                            no_of_personal_tasks=no_of_Task_ID_Personal,
                            category_i=category1, category_ii=category2,
                            category_iii=category3, DateNow = now)
