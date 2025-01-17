from . import mongo, bcrypt

def get_user_by_email(email):
    return mongo.db.users.find_one({"email": email})

def create_user(email, password):
    hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')
    return mongo.db.users.insert_one({"email": email, "password": hashed_pw})

def verify_password(stored_password, provided_password):
    return bcrypt.check_password_hash(stored_password, provided_password)