from flask import Flask
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect
import os

mongo = PyMongo()
bcrypt = Bcrypt()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    print(os.environ.get('SECRET_KEY'))
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    app.config['MONGO_URI'] = 'mongodb://localhost:27017/your_db_name'
    
    mongo.init_app(app)
    bcrypt.init_app(app)
    csrf.init_app(app)

    from .routes import auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app