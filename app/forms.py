from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ClassName(FlaskForm):
    f_variable1 = StringField('Label', validators = [DataRequired()])
    submit = SubmitField()