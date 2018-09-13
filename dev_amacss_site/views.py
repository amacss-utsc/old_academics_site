from dev_amacss_site import app
from flask import render_template, request, jsonify
from dev_amacss_site import api_functions
from werkzeug.security import generate_password_hash, \
     check_password_hash

@app.route("/")
def index():
    return "Hello World"

@app.route("/api/create_user", methods=['POST'])
def create_user():
    if not request.json:
        abort(400)
    elif not (request.json['email'] and request.json['password']):
        abort(400)

    user = {
        "first_name": request.json['fname'],
        "last_name": request.json['lname'],
        "email": request.json['email'],
        "role": request.json['role'],
        "password": generate_password_hash(request.json['password'])
    }
    user_id = api_functions.create_user(user)
    return jsonify({"user_id": user_id}), 201

@app.route("/api/check_password", methods=["GET"])
def check_password():
    if not request.json:
        abort(400)
    elif not (request.json['email'] and request.json['password']):
        abort(400)

    return api_functions.check_password(request.json["email"],
            request.json["password"])


