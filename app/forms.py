from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length

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
	choices = [
		(1, 'App & Games'),
		(2, 'Components'),
		(3, 'Design Concepts')
	]
	title    = StringField('Title', validators=[DataRequired()])
	desc     = StringField('Description', validators=[DataRequired()])
	url      = StringField('Server URL', validators=[DataRequired()])
	img      = StringField('Sample Image')
	category = SelectField('Project Type', validators=[DataRequired()], choices=choices)
	submit   = SubmitField('Add')