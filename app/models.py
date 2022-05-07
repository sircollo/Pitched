import email
from unicodedata import category
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))


class User(UserMixin,db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer,primary_key = True)
  username = db.Column(db.String(255))
  email = db.Column(db.String(255),unique=True,index=True)
  role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
  pass_secure = db.Column(db.String(255))
  Pitches = db.relationship('Pitch',backref = 'user',lazy = 'dynamic')
  upvotes = db.relationship('Upvote',backref='user',lazy='dynamic')

  
  @property
  def password(self):
    raise AttributeError('You cannot read the password attribute')
  
  @password.setter
  def password(self,password):
    self.pass_secure = generate_password_hash(password)
    
  def verify_password(self,password):
    return check_password_hash(self.pass_secure,password)
  
  def __repr__(self):
    return f'User {self.username}'
  
  
class Role(db.Model):
  __tablename__='roles'
  
  id = db.Column(db.Integer,primary_key = True)
  name = db.Column(db.String(255))
  users = db.relationship('User',backref = 'role', lazy='dynamic')
  

  
  def __repr__(self):
    return f'User {self.name}'
  
class Pitch(db.Model):
  __tablename__='pitches'
  id = db.Column(db.Integer,primary_key=True)
  category = db.Column(db.String)
  title = db.Column(db.String)
  pitch = db.Column(db.String(255))
  posted = db.Column(db.DateTime,default=datetime.utcnow)
  user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
  upvotes = db.relationship('Upvote',backref='pitch',lazy='dynamic')
  
  def save_pitch(self):
    db.session.add(self)
    db.session.commit()
    
  @classmethod
  def get_pitches(cls,category):
    pitches = Pitch.query.filter_by(category=category).all()
    return pitches
  
  def __repr__(self):
    return f'Pitch {self.pitch}'
  
  
class Upvote(db.Model):
  __tablename__='upvotes'
  id = db.Column(db.Integer,primary_key=True) 
  upvote_count=  db.Column(db.Integer, default=0)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id',ondelete='SET NULL'),nullable = True)
  pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id',ondelete='SET NULL'),nullable = True) 
  
  def add_upvote(self):
      if self not in db.session:
        db.session.add(self)
        db.session.commit()  
        
  @classmethod
  def get_upvote(cls,pitch_id):
      upvote = Upvote.query.filter_by(pitch_id=pitch_id).first()
      return upvote.upvote_count
  def __repr__(self):
      return f'Upvote {self.pitch}' 

