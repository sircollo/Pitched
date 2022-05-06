import email
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo
from ..models import User
from wtforms import ValidationError

class RegistrationForm(FlaskForm):
  email = StringField('E-mail',validators=[DataRequired(),Email()])
  username = StringField('Username',validators=[DataRequired])
  password = PasswordField('Password',validators=[DataRequired(),EqualTo('password_confirm',message='Password mismatch')])
  password_confirm = PasswordField('Confirm Password',validators=[DataRequired])
  submit = SubmitField('Sign Up')
  
  def validate_email(self,data_field):
    if User.query.filter_by(email=data_field.data).first():
      raise ValidationError('Account with this email exists')
    
  def validate_username(self,data_field):
    if User.query.filter_by(username=data_field.data).first():
      raise ValidationError('Username taken')