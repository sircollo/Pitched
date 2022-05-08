
from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,SubmitField,TextAreaField
from wtforms.validators import DataRequired

CATEGORIES = [('Technology', 'Technology'), ('Farming', 'Farming'), ('Interview', 'Interview'), ('Business', 'Business')]

class PitchForm(FlaskForm):
  title = StringField('Title',validators=[DataRequired()])
  category = SelectField('Category', choices=CATEGORIES,validators=[DataRequired()])
  pitch = TextAreaField('Your Pitch',validators=[DataRequired()])
  submit = SubmitField('Pitch')