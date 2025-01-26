from flask import Flask
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect
import os

mongo = PyMongo()
bcrypt = Bcrypt()
csrf = CSRFProtect()

def create_app():
    if os.environ.get('SECRET_KEY', None) == 'None':
        raise SystemError('SECRET_KEY required')
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    app.config['MONGO_URI'] = 'mongodb://localhost:27017/your_db_name'
    
    mongo.init_app(app)
    bcrypt.init_app(app)
    csrf.init_app(app)

    from .routes import admin_blueprint, auth_blueprint, pages_blueprint
    app.register_blueprint(admin_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(pages_blueprint)

    return app