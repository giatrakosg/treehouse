from flask import Blueprint, jsonify
from database import db
from models.Room import Room, RoomTypes
from models.Image import Image
import random

rooms_blueprint = Blueprint('rooms', __name__)


@rooms_blueprint.route("/rooms", methods=['GET'])
def get_rooms():
    # get_random_data()

    # room = Room(RoomTypes.house, 1, 2, 3, True, 'ok', True, True, True, False,
    # True, False, False, True, True, True, 0, 0, 'ok',
    #             'ok', 2, 3, 4, 3.5, 'Nice Room')
    # db.session.add(room)
    rooms = Room.query.all()
    rooms_dict = []

    for room in rooms:
        rooms_dict.append(room.to_dict_short())

    return jsonify(rooms_dict)


def get_random_data():
    rooms_number = 24
    rooms = []

    for i in range(rooms_number):
        room = Room(random.choice(list(RoomTypes)), random.randint(1, 5), random.randint(1, 5),
                    random.randint(1, 10), bool(random.getrandbits(1)), "desc", bool(random.getrandbits(1)),
                    bool(random.getrandbits(1)), bool(random.getrandbits(1)), bool(random.getrandbits(1)),
                    bool(random.getrandbits(1)), bool(random.getrandbits(1)), bool(random.getrandbits(1)),
                    bool(random.getrandbits(1)), bool(random.getrandbits(1)), bool(random.getrandbits(1)),
                    random.uniform(37.0839412, 38.9839412), random.uniform(23.7283052, 24.7283052),
                    "address", "info", random.randint(1, 5), random.randint(23, 300), random.uniform(10, 70),
                    random.uniform(1, 5), "WOW random title")

        room.images.append(Image('https://picsum.photos/id/' + str(i) + '/400/400', room.id))

        db.session.add(room)

    db.session.commit()
