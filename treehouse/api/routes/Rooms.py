from flask import Blueprint, jsonify, request
from database import db

from models.Room import Room, RoomTypes
from models.Image import Image
from models.Availability import Availability

import random
import time
from datetime import datetime
import string

rooms_blueprint = Blueprint('rooms', __name__)


@rooms_blueprint.route("/rooms", methods=['GET'])
def get_rooms():
    # get_random_data()
    rooms = Room.query.all()
    rooms_dict = []

    date_from = request.args.get('date_from')
    date_to = request.args.get('date_to')

    datetime_from = datetime.strptime(date_from, '%Y-%m-%d')
    datetime_to = datetime.strptime(date_to, '%Y-%m-%d')

    for room in rooms:

        flag = False
        for date_range in room.availabilities:
            if date_range.date_from >= datetime_from and date_range.date_to <= datetime_to:
                flag = True

        if flag:
            rooms_dict.append(room.to_dict_short())

    return jsonify(rooms_dict)


@rooms_blueprint.route("/rooms/<string:room_title>", methods=['GET'])
def get_room(room_title):
    room = Room.query.filter_by(title=room_title).first()

    room_to_dict = room.to_dict_all()

    return jsonify(room_to_dict)


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
                    random.uniform(1, 5), random_title(), random.randint(6, 20), random.randint(1, 3))
        for y in range(10):
            room.images.append(Image('https://picsum.photos/id/' + str(i * 10 + y) + '/400/400'))

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


def random_title():
    letters = string.ascii_letters
    title = ''.join(random.choice(letters) for i in range(6)) + ' ' + ''.join(
        random.choice(letters) for i in range(6)) + ' ' + ''.join(random.choice(letters) for i in range(6))

    return title
