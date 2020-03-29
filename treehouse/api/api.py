
from flask import Flask, request, jsonify, make_response , redirect , url_for
from flask_cors import CORS , cross_origin
from flask_sqlalchemy import SQLAlchemy
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from werkzeug.datastructures import ImmutableMultiDict
import jwt
import datetime
import json
import os
import sys
import markdown
import datetime
from functools import wraps
from schema import Schema, And, Use, Optional
from pprint import pprint

from database import *

#from models.Amenity import Amenity
from models.Availability import Availability
from models.Image import Image
from models.Room import Room
from models.User import User


db.create_all()
#db.session.add(Room('house',1,2,3,True,'ok',True,True,True,0,0,'ok','ok',2,3,4))
db.session.commit()


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message' : 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = User.query.filter_by(public_id=data['public_id']).first()
        except:
            return jsonify({'message' : 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated


@app.route('/', methods=['GET'])
def hello():
    output = ''
    # Open the README file
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:

        # Read the content of the file
        content = markdown_file.read()

        # Convert to HTML
        output += markdown.markdown(content)
    return output

@app.route('/user', methods=['POST','OPTIONS'])
def addUserRequest():

    if request.method == "OPTIONS": # CORS preflight
        return _build_cors_prelight_response()
    elif request.method == "POST": # The actual request following the preflight
        data = request.get_json()
        print(data,file=sys.stderr)
        hashed_password = generate_password_hash(data['password'], method='sha256')

        uEmail = User.query.filter_by(email=data['email']).all()
        if len(uEmail) > 0 :
            return jsonify({'message' : 'Email already exists!'}),400

        isHost = data['isHost']

        new_user = User(
        name=data['name'],
        password=hashed_password,
        surname=data['surname'],
        email=data['email'],
        phone=data['phone'],
        isHost=isHost ,
        isAdmin=False ,
        )

        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message' : 'New user created!'})
    else :
        raise RuntimeError("Weird - don't know how to handle method {}".format(request.method))

def _build_cors_prelight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response

def _corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

if __name__ == '__main__':
    app.run(debug=True)
    cors = CORS(app,resources={r"/api/*": {"origins": "*"}})
    #app.config['CORS_HEADERS'] = 'Content-Type'
    #app.config["CORS_SUPPORTS_CREDENTIALS"] =True
