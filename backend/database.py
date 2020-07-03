# noinspection PyUnresolvedReferences
from flask_sqlalchemy import SQLAlchemy
from flask import Flask ,request, jsonify, make_response , redirect , url_for
# noinspection PyUnresolvedReferences
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager , Server
import sys
import os

from flask_cors import CORS , cross_origin
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from werkzeug.datastructures import ImmutableMultiDict
import jwt
import datetime
import json
import markdown
import datetime
from functools import wraps
from schema import Schema, And, Use, Optional
from pprint import pprint



app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisissecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///backups/treehouse_jul3.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

cors = CORS(app)
db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)

server = Server(port=5000,ssl_crt='./ssl_certificates/cert.pem',ssl_key='./ssl_certificates/key.pem')
manager.add_command('db', MigrateCommand)
manager.add_command('runserver',server)
