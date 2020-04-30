from flask import Blueprint, jsonify, request
from database import db

from models.Room import Room, RoomTypes
from models.Image import Image
from models.Availability import Availability
from models.Review import Review

import json
import random
import time
from datetime import datetime
import string

rooms_blueprint = Blueprint('rooms', __name__)


@rooms_blueprint.route("/rooms/<string:room_title>/update_images", methods=['POST'])
def update_rooms_images(room_title):
    data = request.get_json()

    images_dict = data['images']

    room = Room.query.filter_by(title=room_title).first()
    if room is None:
        return jsonify({'message': 'ERROR'})

    Image.query.filter_by(room_id=room.id).delete()

    for i in images_dict:
        image = Image(i['src'])
        room.images.append(image)

    db.session.commit()

    return jsonify({'message': 'SUCCESS'})


@rooms_blueprint.route("/rooms/host", methods=['GET'])
def get_host_rooms():
    host_rooms_dict = []

    host_id = request.args.get('host_id')

    host_rooms = Room.query.limit(20).all()

    for r in host_rooms:
        host_rooms_dict.append(r.to_dict_host_short())

    return jsonify(host_rooms_dict)


@rooms_blueprint.route("/rooms", methods=['GET'])
def get_rooms():
    # get_random_data()

    rooms_dict = []

    d_from = request.args.get('date_from')
    d_to = request.args.get('date_to')

    datetime_from = datetime.strptime(d_from, '%Y-%m-%d')
    datetime_to = datetime.strptime(d_to, '%Y-%m-%d')

    room_ids = Availability.query.with_entities(Availability.room_id).filter(Availability.date_from >= datetime_from,
                                                                             Availability.date_to <= datetime_to).distinct().all()
    for room_id in room_ids:
        room = Room.query.filter_by(id=room_id[0]).first()
        rooms_dict.append(room.to_dict_short())

    return jsonify(rooms_dict)


@rooms_blueprint.route("/rooms/<string:room_title>", methods=['GET', 'POST', 'DELETE'])
def get_room(room_title):
    room = Room.query.filter_by(title=room_title).first()
    if room is None:
        return jsonify({'message': 'ERROR'})

    if request.method == 'GET':

        room_to_dict = room.to_dict_all()
        return jsonify(room_to_dict)

    elif request.method == 'POST':
        data = request.get_json()
        if data is None:
            return jsonify({'message': 'ERROR'})

        room_d = data['room']
        room.update(json.loads(room_d))

        return jsonify({'message': 'SUCCESS'})
    elif request.method == 'DELETE':
        for a in room.availabilities:
            db.session.delete(a)

        for i in room.images:
            db.session.delete(i)
        for r in room.reviews:
            db.session.delete(r)

        db.session.delete(room)

        db.session.commit()
        return jsonify({'message': 'SUCCESS'})


@rooms_blueprint.route("/rooms/<string:room_title>/new_review", methods=['POST'])
def new_review(room_title):
    data = request.get_json()
    print(data)
    print(room_title)

    room = Room.query.filter_by(title=room_title).first()
    if room is None:
        return jsonify({'message': 'ERROR'})
    print(room)
    room.reviews.append(Review(data['rating'], data['title'], data['description'], 0))
    db.session.commit()

    return jsonify({'message': 'SUCCESS'})


def get_random_data():
    rooms_number = 500
    rooms = []

    for i in range(rooms_number):
        room = Room(random.choice(list(RoomTypes)), random.randint(1, 5), random.randint(1, 5),
                    random.randint(1, 10), bool(random.getrandbits(1)), "desc", bool(random.getrandbits(1)),
                    bool(random.getrandbits(1)), bool(random.getrandbits(1)), bool(random.getrandbits(1)),
                    bool(random.getrandbits(1)), bool(random.getrandbits(1)), bool(random.getrandbits(1)),
                    bool(random.getrandbits(1)), bool(random.getrandbits(1)), bool(random.getrandbits(1)),
                    random.uniform(37.0839412, 38.9839412), random.uniform(23.7283052, 24.7283052),
                    "address", "info", random.randint(1, 5), random.randint(23, 300), random.uniform(10, 70),
                    random_sentence(3), random.randint(6, 20), random.randint(1, 3))
        for y in range(10):
            room.images.append(Image('https://picsum.photos/id/' + str(i * 10 + y) + '/400/400'))
            room.reviews.append(Review(random.uniform(1, 5), random_sentence(3), random_sentence(10), 0))

        for x in range(10):
            date_from = random_date('1/1/2020', '3/12/2020', '%d/%m/%Y', random.random())
            date_to = random_date(date_from, '3/12/2020', '%d/%m/%Y', random.random())

            room.availabilities.append(Availability(datetime.strptime(date_from, '%d/%m/%Y'),
                                                    datetime.strptime(date_to, '%d/%m/%Y')))

        db.session.add(room)

    db.session.commit()


def random_date(start, end, date_format, prop):
    stime = time.mktime(time.strptime(start, date_format))
    etime = time.mktime(time.strptime(end, date_format))

    ptime = stime + prop * (etime - stime)
    return time.strftime(date_format, time.localtime(ptime))


def random_sentence(words_number):
    letters = string.ascii_letters

    sentence = ''

    for x in range(words_number):
        word = ''.join(random.choice(letters) for i in range(6))

        sentence = sentence + ' ' + word

    return sentence
