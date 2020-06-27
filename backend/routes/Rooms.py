from flask import Blueprint, jsonify, request
from database import db

from models.Room import Room, RoomTypes
from models.Image import Image
from models.Reservation import Reservation, Status
from models.Review import Review
from models.Thread import Thread
from models.User import User
from models.Message import Message

import json
import random
import time
from datetime import datetime, timedelta
import string

rooms_blueprint = Blueprint('rooms', __name__)


@rooms_blueprint.route("/rooms/<int:room_id>/update_images", methods=['POST'])
def update_rooms_images(room_id):
    data = request.get_json()

    images_dict = data['images']

    room = Room.query.filter_by(id=room_id).first()
    if room is None:
        return jsonify({'message': 'ERROR'})

    Image.query.filter_by(room_id=room.id).delete()

    for i in images_dict:
        image = Image(i['src'])
        room.images.append(image)

    db.session.commit()

    return jsonify({'message': 'SUCCESS'})


@rooms_blueprint.route("/rooms/host/<string:public_host_id>", methods=['GET'])
def get_host_rooms(public_host_id):
    host_rooms_dict = []

    host = User.query.filter_by(public_id=public_host_id).first()

    host_rooms = Room.query.filter_by(owner_id=host.id)

    if host_rooms is None:
        return jsonify({'message': 'ERROR'})

    for r in host_rooms:
        host_rooms_dict.append(r.to_dict_host_short())

    return jsonify(host_rooms_dict)


@rooms_blueprint.route("/rooms/<room_id>", methods=['GET', 'PATCH', 'DELETE', 'POST'])
def get_room(room_id):
    if request.method == 'GET':

        room = Room.query.filter_by(id=room_id).first()

        if room is None:
            return jsonify({'message': 'ERROR'})

        room_to_dict = room.to_dict_all()
        print(room_to_dict)

        return jsonify(room_to_dict)

    elif request.method == 'PATCH':

        room = Room.query.filter_by(id=room_id).first()

        data = request.get_json()

        if data is None:
            return jsonify({'message': 'ERROR'})

        room_d = data['room']

        room.update(room_d)

        return jsonify({'message': 'SUCCESS'})
    elif request.method == 'POST':

        data = request.get_json()
        print(data)

        if data is None:
            return jsonify({'message': 'ERROR'})

        room_dict = data['room']

        owner_id = room_dict['public_owner_id']
        owner = User.query.filter_by(public_id=owner_id).first()

        room = Room(room_dict['type'], room_dict['beds_num'], room_dict['baths_num'], room_dict['bedrooms_num'],
                    room_dict['lounge'], room_dict['description'], room_dict['smoking_allowed'],
                    room_dict['pets_allowed'], room_dict['events_allowed'], room_dict['wireless_internet'],
                    room_dict['air_condition'], room_dict['refrigerator'], room_dict['kitchen'], room_dict['tv'],
                    room_dict['parking'], room_dict['elevator'], room_dict['location'][0], room_dict['location'][1],
                    room_dict['address'], room_dict['transport_info'], room_dict['persons_number'],
                    room_dict['elevator'], room_dict['cost_per_day'], room_dict['title'], room_dict['area'],
                    room_dict['min_stay'], owner.id)

        db.session.add(room)
        db.session.commit()

        return jsonify({'room_id': room.id})

    elif request.method == 'DELETE':

        room = Room.query.filter_by(id=room_id).first()

        if room is None:
            return jsonify({'message': 'ERROR'})

        for a in room.reservations:
            db.session.delete(a)

        for t in room.threads:
            t.destroy()
            db.session.delete(t)

        for i in room.images:
            db.session.delete(i)
        for r in room.reviews:
            db.session.delete(r)

        db.session.delete(room)

        db.session.commit()
        return jsonify({'message': 'SUCCESS'})


@rooms_blueprint.route("/rooms", methods=['GET'])
def get_rooms():
    # get_random_data()

    rooms_dict = []

    d_from = request.args.get('date_from')
    d_to = request.args.get('date_to')
    datetime_from = datetime.strptime(d_from, '%Y-%m-%d')
    datetime_to = datetime.strptime(d_to, '%Y-%m-%d')

    location = [float(request.args.get('lat')), float(request.args.get('long'))]

    location_rooms = search_rooms_in_area(location)

    if len(location_rooms):

        for room in location_rooms:
            flag = False
            for r in room.reservations:

                if r.date_from > datetime_to or r.date_to < datetime_from:
                    print(str(r.date_from) + ' ' + str(r.date_to))
                    flag = True
            if flag:
                rooms_dict.append(room.to_dict_short())

    return jsonify(rooms_dict)


def search_rooms_in_area(location):
    radius = 0.3
    bounds_1 = [location[0] + radius, location[1] + radius]
    bounds_2 = [location[0] - radius, location[1] - radius]

    close_rooms = Room.query.filter(
        (bounds_2[0] <= Room.lat_coordinate) & (Room.lat_coordinate <= bounds_1[0]),
        (bounds_2[1] <= Room.long_coordinate) & (Room.long_coordinate <= bounds_1[1])).all()

    return close_rooms


def get_random_data():
    rooms_number = 300
    rooms = []

    for i in range(rooms_number):
        room = Room(random.choice(list(RoomTypes)), random.randint(1, 5), random.randint(1, 5),
                    random.randint(1, 10), bool(random.getrandbits(1)), "desc", bool(random.getrandbits(1)),
                    bool(random.getrandbits(1)), bool(random.getrandbits(1)), bool(random.getrandbits(1)),
                    bool(random.getrandbits(1)), bool(random.getrandbits(1)), bool(random.getrandbits(1)),
                    bool(random.getrandbits(1)), bool(random.getrandbits(1)), bool(random.getrandbits(1)),
                    37.9754983 + random.uniform(-1, 1), 23.7356671 + random.uniform(-1, 1),
                    "address", "info", random.randint(1, 5), random.randint(23, 300), random.uniform(10, 70),
                    random_sentence(3), random.randint(6, 20), random.randint(1, 3), 3)
        for z in range(30):
            t = Thread(3, random.randint(1, 2) * 2)

            t.get_random_messages()

            room.threads.append(t)

        for y in range(10):
            room.images.append(Image('https://picsum.photos/id/' + str(i * 10 + y) + '/400/400'))
            room.reviews.append(
                Review(random.uniform(1, 5), random_sentence(3), random_sentence(10), random.randint(1, 2) * 2))

        start_date = datetime.now()

        for x in range(10):
            next_date = start_date + timedelta(days=random.randint(2, 30))

            room.reservations.append(Reservation(start_date, next_date, Status.rented))

            start_date = next_date + timedelta(days=random.randint(20, 40))

        next_date = None
        room.reservations.append(Reservation(start_date, next_date, Status.not_available))

        db.session.add(room)

    db.session.commit()


def random_sentence(words_number):
    letters = string.ascii_letters

    sentence = ''

    for x in range(words_number):
        word = ''.join(random.choice(letters) for i in range(6))

        sentence = sentence + ' ' + word

    return sentence
