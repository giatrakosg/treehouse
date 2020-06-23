from flask import Blueprint, jsonify, request
from database import db

from models.Thread import Thread
from models.Message import Message
from models.Room import Room

from datetime import datetime, timedelta
import json

messages_blueprint = Blueprint('messages', __name__)


@messages_blueprint.route("/threads/<int:thread_id>/messages", methods=['POST', 'GET', 'DELETE', 'PUT'])
def thread_messages(thread_id):
    args_data = request.get_json()
    print(args_data)

    if request.method == 'GET':

        thread = Thread.query.filter_by(id=thread_id).first()

        if thread is None:
            return jsonify({'message': 'ERROR'})

        thread.messages[-1].is_read = True

        messages = thread.to_dict()
        db.session.commit()

        return jsonify(messages)

    if request.method == 'POST':

        thread = Thread.query.filter_by(id=thread_id).first()

        print(thread)

        if thread is None:
            return jsonify({'message': 'ERROR'})

        message_data = json.loads(args_data['message'])

        format_date = datetime.strptime(message_data['timestamp'], '%d/%m/%Y %H:%M')

        message = Message(False, format_date, message_data['text'])
        thread.messages.append(message)
    elif request.method == 'PUT':
        room_title = json.loads(args_data['room_title'])
        print(room_title)

        room = Room.query.filter_by(title=room_title).first()
        thread = Thread()
        room.threads.append(thread)

        message_data = json.loads(args_data['message'])

        format_date = datetime.strptime(message_data['timestamp'], '%d/%m/%Y %H:%M')

        message = Message(False, format_date, message_data['text'])
        thread.messages.append(message)
        print(message)

    elif request.method == 'DELETE':

        thread = Thread.query.filter_by(id=thread_id).first()

        print(thread)

        if thread is None:
            return jsonify({'message': 'ERROR'})

        message_id = json.loads(args_data['message_id'])

        del_message = Message.query.filter_by(id=message_id).first()

        if del_message is None:
            return jsonify({'message': 'ERROR'})

        db.session.delete(del_message)
        if not thread.messages:
            db.session.delete(thread)

        print(thread.messages)

    db.session.commit()
    return jsonify({'message': 'SUCCESS'})


@messages_blueprint.route("/rooms/<int:room_id>/threads", methods=['GET'])
def get_threads(room_id):
    room = Room.query.filter_by(id=room_id).first()

    if room is None:
        return jsonify({'message': 'ERROR'})

    threads_dict = []
    threads = room.threads

    for t in threads:
        threads_dict.append(t.to_dict())

    return jsonify(threads_dict)
