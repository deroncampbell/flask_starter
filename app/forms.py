from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import (StringField, SubmitField, SelectField, TextField, TextAreaField)
from wtforms.validators import DataRequired


class myForm(FlaskForm):
    title = TextField('Property Title',validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    rooms = TextField('No. of Rooms', validators=[DataRequired()])
    brooms = TextField('No. of Bathrooms', validators=[DataRequired()])
    price = TextField('Price', validators=[DataRequired()])
    property_type = SelectField(u'Property Type', choices= [('h','House'),('a','Apartment')],validators=[DataRequired()])
    location = TextField('Location', validators=[DataRequired()])
    photo = FileField('Photo',validators=[FileRequired(),FileAllowed(['jpg','png','jpeg'], 'Images only!')])
    

