from flask import Blueprint, jsonify
from database import db
from models.Room import Room
from models.Image import Image

rooms_blueprint = Blueprint('rooms', __name__)


@rooms_blueprint.route("/rooms", methods=['GET'])
def get_rooms():
    room = Room('house', 1, 2, 3, True, 'ok', True, True, True, False, True, False, False, True, True, True, 0, 0, 'ok',
                'ok', 2, 3, 4, 3.5, 'Nice Room')
    db.session.add(room)
    room.images.append(Image("https://cdn.vuetifyjs.com/images/cards/docks.jpg", room.id))

    return jsonify(room.to_dict_short())
