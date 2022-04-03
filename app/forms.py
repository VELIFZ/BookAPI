from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class Search(FlaskForm):
    name = StringField('Type Author or book name', validators = [DataRequired()])
    submit = SubmitField()