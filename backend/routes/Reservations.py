from flask import Blueprint, jsonify, request
from database import db

from models.Room import Room, RoomTypes
from models.Image import Image
from models.Reservation import Reservation, Status
from models.User import User
from models.Review import Review
from models.Thread import Thread
from models.Message import Message

import json
import random
import time
from datetime import datetime, timedelta
import string

reservations_blueprint = Blueprint('reservations', __name__)


@reservations_blueprint.route("/rooms/<int:room_id>/reservations/unavailable_dates", methods=['GET', 'POST'])
def unavailable_dates(room_id):
    if request.method == 'GET':
        room = Room.query.filter_by(id=room_id).first()

        if room is None:
            return jsonify({'message': 'ERROR'})

        reservations_dict = []
        for i in room.reservations:
            if i.status == Status.not_available:
                reservations_dict.append(i.to_dict())
        return jsonify(reservations_dict)
    elif request.method == 'POST':
        room = Room.query.filter_by(id=room_id).first()

        new_reservations = request.get_json()
        print(new_reservations)
        new_reservations = new_reservations['new_reservations']

        reservations = new_reservations['reservations']
        renter_public_id = new_reservations['public_user_id']
        renter = User.query.filter_by(public_id=renter_public_id).first()

        if room is None:
            return jsonify({'message': 'ERROR'})

        for r in room.reservations:
            db.session.delete(r)
        for a in reservations:
            d_from = datetime.strptime(a['date_from'], "%Y-%m-%d")
            if a['date_to'] is None:
                d_to = None
            else:
                d_to = datetime.strptime(a['date_to'], "%Y-%m-%d")

            room.reservations.append(Reservation(d_from, d_to, Status.not_available, renter.id))

        db.session.commit()
        return jsonify({'message': 'SUCCESS'})


@reservations_blueprint.route("/rooms/<int:room_id>/reservations", methods=['GET', 'PUT'])
def set_reservations(room_id):
    if request.method == 'GET':
        room = Room.query.filter_by(id=room_id).first()

        if room is None:
            return jsonify({'message': 'ERROR'})

        reservations_dict = []
        for i in room.reservations:
            reservations_dict.append(i.to_dict())
        return jsonify(reservations_dict)

    elif request.method == 'PUT':
        room = Room.query.filter_by(id=room_id).first()

        if room is None:
            return jsonify({'message': 'ERROR'})

        new_reservation = request.get_json()
        new_reservation = new_reservation['reservation']

        d_from = datetime.strptime(new_reservation['date_from'], "%Y-%m-%d")
        if new_reservation['date_to'] is None:
            d_to = None
        else:
            d_to = datetime.strptime(new_reservation['date_to'], "%Y-%m-%d")

        renter_public_id = new_reservation['public_user_id']
        renter = User.query.filter_by(public_id=renter_public_id).first()

        room.reservations.append(Reservation(d_from, d_to, Status.rented, renter.id))

        db.session.commit()
        return jsonify({'message': 'SUCCESS'})
