from flask import render_template
from . import main
from flask_login import login_required
from flask_login import login_required
from .. import db
from ..models import User,Pitch

@main.route('/home')
def index():
  pitches_list = Pitch.query.all()
  return render_template('index.html',pitches_list=pitches_list)



