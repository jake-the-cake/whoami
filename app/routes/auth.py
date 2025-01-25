from flask import Blueprint, request, redirect, session, url_for
from app.models import get_user_by_email, create_user, verify_password

auth_blueprint = Blueprint('auth', __name__)

def set_error(error):
  session['user'] = { 'error': error }

def user_exists(email): set_error(f'{ email } is already registered.')
def invalid_email(email): set_error(f'{ email } is not registered.' )
def invalid_password(): set_error('Invalid password.')

def set_user(user):
  user['_id'] = str(user['_id'])
  session['user'] = user

@auth_blueprint.route('/register', methods=['POST'])
def register():
  email = request.form.get('email', '')
  user = get_user_by_email(email)
  if user:
    user_exists(email)
  else:
    create_user(email, request.form.get('password'))
    set_user(get_user_by_email(email))
  return redirect(request.referrer)

@auth_blueprint.route('/login', methods=['POST'])
def login():
  email = request.form.get('email', '')
  user = get_user_by_email(email)
  if user:
    if verify_password(user['password'], request.form.get('password', '')):
      set_user(user)
    else: invalid_password()
  else: invalid_email(email)
  return redirect(request.referrer)