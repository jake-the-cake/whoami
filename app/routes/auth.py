from flask import Blueprint, request, redirect, session, render_template_string, flash
from app.models import get_user_by_email, create_user, verify_password, set_user, new_message
from app.errors import invalid_email, invalid_password, user_exists

auth_blueprint = Blueprint('auth', __name__)

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

@auth_blueprint.route('/logout', methods=['GET'])
def logout():
  session.pop('user', None)
  return redirect(request.referrer)

@auth_blueprint.route('/dashboard', methods=['GET'])
def dashboard():
  return render_template_string('Dashboard Coming Soon...')