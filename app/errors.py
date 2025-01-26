from flask import session

def set_session_error(error):
  session['user'] = { 'error': error }

def user_exists(email): set_session_error(f'{ email } is already registered.')

def invalid_email(email): set_session_error(f'{ email } is not registered.' )

def invalid_password(): set_session_error('Invalid password.')