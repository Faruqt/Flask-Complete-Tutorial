from flask_wtf import FlaskForm
from wtforms import StringField, TimeField, DateField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from .models import Category

class TaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    category = SelectField('Category', coerce=int , validators=[DataRequired()])
    date = DateField('Date', format='%Y-%m-%d' , validators=[DataRequired()])
    time = TimeField('Time', format='%H:%M' , validators=[DataRequired()])
    submit = SubmitField('Add task')

