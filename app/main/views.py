from flask import render_template
from . import main
from flask_login import login_required
from flask_login import login_required
from .. import db

@main.route('/home')
def index():
  return render_template('index.html')



