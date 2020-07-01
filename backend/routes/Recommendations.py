from flask import Blueprint, jsonify, request
from database import db

from models.Room import Room, RoomTypes
from models.User import User
from models.Recommendation import Recommendation
from routes.Users import token_required

import json
import random
import time
from datetime import datetime, timedelta
import string

recommendations_blueprint = Blueprint('recommendations', __name__)


@recommendations_blueprint.route("/recs/<public_id>", methods=['GET'])
@token_required
def get_recommendations(current_user,public_id):
    user = User.query.filter_by(public_id=public_id).first()

    if user is None:
        return jsonify({'message': 'ERROR'})

    recs = Recommendation.query.filter_by(uid=user.id).all()
    recs_dict = []
    for rec in recs :
        recs_dict.append(rec.to_dict())
    return jsonify(recs_dict)
