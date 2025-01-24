from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from .forms import RegistrationForm, LoginForm
from .models import get_user_by_email, create_user, verify_password
from . import mongo

auth_blueprint = Blueprint('auth', __name__)
pages_blueprint = Blueprint('pages', __name__)

def use_login_form() -> LoginForm:
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = get_user_by_email(email)
        if user and verify_password(user['password'], password):
            flash('Login successful!', 'success')
            return redirect(url_for('auth.dashboard'))  # Define a dashboard route later
        else:
            flash('Invalid email or password.', 'danger')
    return form

@pages_blueprint.route('/about')
def about():
    return render_template('index.html')

@pages_blueprint.route('/contact')
def contact():
    return render_template('index2.html')

@pages_blueprint.route('/projects', methods=['GET', 'POST'])
def projects():
    register = RegistrationForm()
    return render_template('projects.html', login=use_login_form(), register = register)

@pages_blueprint.route('/')
def home():
    return render_template('home.html')

# routes requiring auth validations
@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        
        if get_user_by_email(email):
            flash('Email is already registered.', 'danger')
        else:
            create_user(email, password)
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('auth.login'))
    
    return render_template('register.html', form=form)

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html', form=use_login_form())

@pages_blueprint.route('/data')
def data():
    users = []
    for user in mongo.db.users.find():
        user['_id'] = str(user['_id'])
        users.append(user)
    return jsonify(users)