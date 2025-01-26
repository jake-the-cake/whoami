from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, session
from app.forms import RegistrationForm, LoginForm, AddProjectForm
from app.models import parse_choices
from app import mongo


pages_blueprint = Blueprint('pages', __name__)

@pages_blueprint.route('/about')
def about():
    return render_template('index.html')

@pages_blueprint.route('/contact')
def contact():
    return render_template('index2.html')

@pages_blueprint.route('/projects', methods=['GET', 'POST'])
def projects():
	user = session.get('user', None)
	projects = mongo.db.projects.find()
	register = RegistrationForm()
	return render_template('projects.html', 
												login=LoginForm(), 
												register = register, 
												user=user, 
												apps=( app for app in projects if app['category'] == '1'))

@pages_blueprint.route('/')
def home():
    return render_template('home.html')

@pages_blueprint.route('/data')
def data():
	users = []
	projects = []
	for project in mongo.db.projects.find():
		project['_id'] = str(project['_id'])
		project['category'] = parse_choices(project['category'], AddProjectForm.choices)
		projects.append(project)
	for user in mongo.db.users.find():
		user['_id'] = str(user['_id'])
		users.append(user)
	return jsonify(users + projects)