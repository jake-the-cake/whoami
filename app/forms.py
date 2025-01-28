from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from app.models import project_types

class RegistrationForm(FlaskForm):
	email            = StringField('Email', validators=[DataRequired(), Email(), Length(max=100)])
	password         = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
	submit           = SubmitField('Register')

class LoginForm(FlaskForm):
	email    = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit   = SubmitField('Login')
    
class AddProjectForm(FlaskForm):
	title    = StringField('Title', validators=[DataRequired()])
	desc     = StringField('Description', validators=[DataRequired()])
	url      = StringField('Server URL', validators=[DataRequired()])
	img      = StringField('Sample Image')
	category = SelectField('Project Type', validators=[DataRequired()], choices=project_types)
	submit   = SubmitField('Add')

class ContactForm(FlaskForm):
	name    = StringField('Your Name', validators=[DataRequired()])
	email   = StringField('Email', validators=[DataRequired(), Email()])
	message = TextAreaField('What can I do for you?', validators=[DataRequired()])
	submit  = SubmitField('Send')