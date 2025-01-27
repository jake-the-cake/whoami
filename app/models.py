from . import mongo, bcrypt
from flask import session
from bson import ObjectId

def get_user_by_email(email):
	return mongo.db.users.find_one({"email": email})

def create_user(email, password):
	hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')
	return mongo.db.users.insert_one({"email": email, "password": hashed_pw})

def verify_password(stored_password, provided_password):
	return bcrypt.check_password_hash(stored_password, provided_password)

def create_project(title, desc, url, img, category):
	return mongo.db.projects.insert_one({
		'title': title,
		'desc': desc,
		'url': url,
		'img': img,
		'category': category
	})

def delete_project_by_id(id: str) -> dict:
	if get_project_by_id(id): mongo.db.projects.delete_one({'_id': ObjectId(id)})

def get_project_by_id(id: str) -> dict:
	return mongo.db.projects.find_one(ObjectId(id))

def parse_choices(index: str, choices: list):
	print(choices)
	return next((value[1] for value in choices if str(value[0]) == index), None)

def set_user(user):
  user['_id'] = str(user['_id'])
  session['user'] = user