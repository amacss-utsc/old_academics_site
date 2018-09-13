from dev_amacss_site import app
from pymongo import MongoClient
from flask import jsonify
from werkzeug.security import generate_password_hash, \
     check_password_hash

import sys

client = MongoClient('mongodb://localhost:27017/')
db = client['amacss_site']
users = db.users

def create_user(user):
    user_id = users.insert_one(user).inserted_id
    return str(user_id)

def check_password(email, password):
    '''Will return 200 and password check status if email is found,
    404 otherwise'''
    user = { 'email': email }
    found_user = users.find_one(user)
    if found_user:
        return jsonify({"status":
                check_password_hash(found_user["password"], password)}), 200
    return jsonify({"status": "NOT FOUND"}), 404