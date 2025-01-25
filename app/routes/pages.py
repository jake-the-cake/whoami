from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, session
from app.forms import RegistrationForm, LoginForm
from app.models import get_user_by_email, verify_password
from app import mongo

pages_blueprint = Blueprint('pages', __name__)

def use_login_form() -> LoginForm:
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = get_user_by_email(email)
        if user and verify_password(user['password'], password):
            session['user'] = user
        else:
            session['user'] = { 'error': 'Invalid login credentials.' }
        return redirect(request.referrer)  # Define a dashboard route later
    return form

@pages_blueprint.route('/about')
def about():
    return render_template('index.html')

@pages_blueprint.route('/contact')
def contact():
    return render_template('index2.html')

@pages_blueprint.route('/projects', methods=['GET', 'POST'])
def projects():
    user = session.get('user', None)
    print(user)
    register = RegistrationForm()
    return render_template('projects.html', login=use_login_form(), register = register, user=user)

@pages_blueprint.route('/')
def home():
    return render_template('home.html')

@pages_blueprint.route('/data')
def data():
    users = []
    for user in mongo.db.users.find():
        user['_id'] = str(user['_id'])
        users.append(user)
    return jsonify(users)