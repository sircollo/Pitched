from flask import render_template
from . import main
from flask_login import login_required
from flask_login import login_required
from .. import db
from ..models import User,Pitch

@main.route('/home')
def index():
  pitches_list = Pitch.query.all()
  business_pitch = Pitch.query.filter_by(category = 'Business').all()
  technology_pitch = Pitch.query.filter_by(category = 'Technology').all()
  interview_pitch = Pitch.query.filter_by(category = 'Interview').all()
  farming_pitch = Pitch.query.filter_by(category='Farming').all()
  return render_template('index.html',pitches_list=pitches_list,business_pitch=business_pitch,interview_pitch=interview_pitch,technology_pitch=technology_pitch, farming_pitch=farming_pitch)