from flask import Blueprint

task = Blueprint('task', __name__, template_folder='templates')

from . import views
