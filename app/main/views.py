from flask import render_template,redirect,url_for,abort,request
from . import main
from flask_login import login_required
from flask_login import login_required,current_user
from .. import db,photos
from ..models import User,Pitch,Upvote,Downvote,Comment
from .forms import PitchForm,UpdateProfile,CommentsForm
import markdown2

@main.route('/home')
@login_required
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
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first() 
    user_pitches = Pitch.query.filter_by(user_id =current_user._get_current_object().id ).all()  

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user,user_pitches=user_pitches)


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
@main.route('/upvote/<int:user_id>/<int:pitch_id>')
def upvote(pitch_id,user_id):
    upvote = Upvote.query.filter_by(user_id =current_user._get_current_object().id).first()   
    print(pitch_id)
    if upvote:
        pitch_id = pitch_id
       
        if upvote.user_id == current_user._get_current_object().id and upvote.pitch_id == pitch_id :         
            return redirect(url_for("main.index"))
        elif  upvote.pitch_id == pitch_id  and db.session.query(Upvote.id).filter_by(user_id=current_user._get_current_object().id) is not None   :
            return redirect(url_for("main.index")) 
        else:
            print(pitch_id)
            pitch_id = pitch_id
            user_id = current_user._get_current_object().id
            upvote_count = 1
            new_upvote = Upvote(upvote_count=upvote_count,user_id = user_id,pitch_id = pitch_id)
            new_upvote.add_upvote()
            return redirect(url_for("main.index"))

    else:
        pitch_id = pitch_id
        user_id = current_user._get_current_object().id
        upvote_count = 1
        new_upvote = Upvote(upvote_count=upvote_count,user_id = user_id,pitch_id = pitch_id)
        new_upvote.add_upvote()
        
       
    return redirect(url_for("main.index"))
  
@main.route('/downvote/<int:user_id>/<int:pitch_id>')
def downvote(pitch_id,user_id):
    downvote = Downvote.query.filter_by(user_id =current_user._get_current_object().id).first()
   
    print(pitch_id)
    if downvote:
        pitch_id = pitch_id
      
        if downvote.user_id == current_user._get_current_object().id and downvote.pitch_id == pitch_id :         
            return redirect(url_for("main.index"))
        elif  downvote.pitch_id == pitch_id  and db.session.query(Downvote.id).filter_by(user_id=current_user._get_current_object().id) is not None   :
            return redirect(url_for("main.index")) 
        else:
            print(pitch_id)
            pitch_id = pitch_id
            user_id = current_user._get_current_object().id
            downvote_count = 1
            new_downvote = Downvote(downvote_count=downvote_count,user_id = user_id,pitch_id = pitch_id)
            new_downvote.add_downvote()
            return redirect(url_for("main.index"))
   
    else:
        pitch_id = pitch_id
        user_id = current_user._get_current_object().id
        downvote_count = 1
        new_downvote = Downvote(downvote_count=downvote_count,user_id = user_id,pitch_id = pitch_id)
        new_downvote.add_downvote()

       
    return redirect(url_for("main.index"))
  
@main.route('/comment/<int:pitch_id>', methods = ['POST','GET'])
@login_required
def comment(pitch_id):
    form = CommentsForm()
    pitch = Pitch.query.get(pitch_id)
    comments = Comment.query.filter_by(pitch_id = pitch_id).all()
    if form.validate_on_submit():
        comment = form.comment.data 
        pitch_id = pitch_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment = comment,user_id = user_id,pitch_id = pitch_id)
        new_comment.save_comment()
        return redirect(url_for('.comment', pitch_id = pitch_id))
    return render_template('comments.html', form =form, pitch = pitch,comments=comments)
