from flask import Blueprint, jsonify, request
from database import db

from models.Thread import Thread
from models.Message import Message
from models.Room import Room

from datetime import datetime, timedelta
import json

messages_blueprint = Blueprint('messages', __name__)


@messages_blueprint.route("/threads/<int:thread_id>/message", methods=['POST', 'DELETE', 'PUT'])
def new_message(thread_id):
    args_data = request.get_json()
    print(args_data)

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


@messages_blueprint.route("/threads/<int:thread_id>", methods=['GET'])
def get_thread_messages(thread_id):
    thread = Thread.query.filter_by(id=thread_id).first()

    if thread is None:
        return jsonify({'message': 'ERROR'})

    thread_messages = Message.query.filter_by(thread_id=thread_id, is_read=False).all()
    for m in thread_messages:
        m.is_read = True
        db.session.commit()

    messages = thread.to_dict()

    return jsonify(messages)
