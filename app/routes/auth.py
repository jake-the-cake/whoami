from flask import Blueprint, render_template, request, redirect, url_for, session
from app.forms import RegistrationForm, LoginForm
from app.models import get_user_by_email, create_user, verify_password

auth_blueprint = Blueprint('auth', __name__)

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
    return redirect(request.referrer)
  return form

@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    email = form.email.data
    password = form.password.data
    
    if get_user_by_email(email):
      session['user'] = {
        'error': 'Email is already registered.'
      }
    else:
      create_user(email, password)
      return redirect(url_for('auth.login'))
    
    return render_template('register.html', form=form)

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
  form = request.form
  user = get_user_by_email(form.get('email'))
  if user and verify_password(user['password'], form['password']):
    user['_id'] = str(user['_id'])
    session['user'] = user
  print(form)
  return redirect(request.referrer)