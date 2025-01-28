from flask import Blueprint, render_template, jsonify, session
from app.forms import RegistrationForm, LoginForm, ContactForm
from app.models import parse_choices
from app import mongo


pages_blueprint = Blueprint('pages', __name__)

@pages_blueprint.route('/about')
def about():
    return render_template('about.html')

@pages_blueprint.route('/contact')
def contact():
    return render_template('contact.html', form=ContactForm())

@pages_blueprint.route('/projects', methods=['GET', 'POST'])
def projects():
	projects = mongo.db.projects.find()
	lists = [[] for _ in range(3)]
	for p in projects: lists[int(p.get('category', 1)) - 1].append(p)
	return render_template('projects.html', 
									login=LoginForm(), 
									register = RegistrationForm(), 
									user=session.get('user', None), 
									apps=lists[0],
									components=lists[1],
									concepts=lists[2])

@pages_blueprint.route('/')
def home():
    return render_template('home.html')

@pages_blueprint.route('/data')
def data():
	users = []
	projects = []
	for project in mongo.db.projects.find():
		project['_id'] = str(project['_id'])
		project['category'] = parse_choices(project['category'])
		projects.append(project)
	for user in mongo.db.users.find():
		user['_id'] = str(user['_id'])
		users.append(user)
	return jsonify(users + projects)