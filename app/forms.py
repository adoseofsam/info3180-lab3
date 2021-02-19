from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email
from wtforms import StringField,TextAreaField
from flask_wtf.file import FileField, FileRequired, FileAllowed

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    subject = StringField('Subject', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message',validators=[DataRequired()])