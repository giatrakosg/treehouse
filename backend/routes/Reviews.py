from flask import Blueprint, jsonify, request
from database import db

from models.Room import Room, RoomTypes
from models.Image import Image
from models.Reservation import Reservation, Status
from models.Review import Review
from models.Thread import Thread
from models.Message import Message
from models.User import User

import json
import random
import time
from datetime import datetime, timedelta
import string

reviews_blueprint = Blueprint('reviews', __name__)


@reviews_blueprint.route("/rooms/<int:room_id>/reviews", methods=['GET'])
def get_reviews(room_id):
    print(room_id)
    reviews_dict = []
    room = Room.query.filter_by(id=room_id).first()
    if room is None:
        return jsonify({'message': 'ERROR'})

    for i in room.reviews:
        reviews_dict.append(i.to_dict())
    print(reviews_dict)

    return jsonify(reviews_dict)


@reviews_blueprint.route("/rooms/<int:room_id>/new_review", methods=['POST'])
def new_review(room_id):
    data = request.get_json()

    room = Room.query.filter_by(id=room_id).first()
    if room is None:
        return jsonify({'message': 'ERROR'})
    print(data)
    review = data['review']

    user_public_id = review['user_public_id']
    user = User.query.filter_by(public_id=user_public_id).first()
    user_id = user.id
    print(user_id)

    room.reviews.append(Review(review['rating'], review['title'], review['description'], user_id))
    db.session.commit()

    return jsonify({'message': 'SUCCESS'})
