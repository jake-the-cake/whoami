from flask import Blueprint, render_template, request, redirect, url_for, flash
from .forms import RegistrationForm, LoginForm
from .models import get_user_by_email, create_user, verify_password

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/a', methods=['GET', 'POST'])
def home1():
    return render_template('index.html')

@auth_blueprint.route('/b', methods=['GET', 'POST'])
def home2():
    return render_template('index2.html')

@auth_blueprint.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

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

    return render_template('login.html', form=form)