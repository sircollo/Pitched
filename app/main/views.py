from flask import render_template,redirect,url_for,abort,request
from . import main
from flask_login import login_required
from flask_login import login_required,current_user
from .. import db,photos
from ..models import User,Pitch,Upvote,Downvote
from .forms import PitchForm,UpdateProfile

@main.route('/home')
def index():
  pitches_list = Pitch.query.all()
  business_pitch = Pitch.query.filter_by(category = 'Business').all()
  technology_pitch = Pitch.query.filter_by(category = 'Technology').all()
  interview_pitch = Pitch.query.filter_by(category = 'Interview').all()
  farming_pitch = Pitch.query.filter_by(category='Farming').all()
  return render_template('index.html',pitches_list=pitches_list,business_pitch=business_pitch,interview_pitch=interview_pitch,technology_pitch=technology_pitch, farming_pitch=farming_pitch)

@main.route('/new_pitch',methods= ['GET','POST'])
@login_required
def new_pitch():
    form = PitchForm()    
    if form.validate_on_submit():
        title = form.title.data
        pitch = form.pitch.data
        category = form.category.data
        user_id = current_user
        new_pitch_object = Pitch(pitch=pitch,user_id=current_user._get_current_object().id,category=category,title=title)
        new_pitch_object.save_pitch()
       
        return redirect(url_for('main.index'))
    
    return render_template('new_pitch.html',form=form)
  
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))
