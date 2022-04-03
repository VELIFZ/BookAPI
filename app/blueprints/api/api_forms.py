from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, DecimalField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed, FileField

# With this form, user's can add books they want to sell. Then it will be in the DB and API 

class SellForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    condition = StringField('Condition', validators=[DataRequired()])
    description = StringField('Description')
    price = DecimalField('Price')
    image = FileField('Image') #, validators=[FileAllowed('jpg', 'png', 'gif', 'jpeg')]
    publisher = StringField('Publisher')
    publish_year = StringField('Publish Year')
    categories = StringField('Category')
    
    submit = SubmitField()

# class UploadForm(Form):
#     image        = FileField(u'Image File', [validators.regexp(u'^[^/\\]\.jpg$')])
#     description  = TextAreaField(u'Image Description')

#     def validate_image(form, field):
#         if field.data:
#             field.data = re.sub(r'[^a-z0-9_.-]', '_', field.data)

#     def upload(request):
#         form = UploadForm(request.POST)
#         if form.image.data:
#             image_data = request.FILES[form.image.name].read()
#             open(os.path.join(UPLOAD_PATH, form.image.data), 'w').write(image_data)