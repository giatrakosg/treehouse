from flask import Blueprint, jsonify, request
from database import db

from models.Thread import Thread
from models.Message import Message
from models.Room import Room
from models.User import User

from datetime import datetime, timedelta
import json

messages_blueprint = Blueprint('messages', __name__)


@messages_blueprint.route("/threads/thread/new_message", methods=['POST'])
def new_thread_message():
    user1_id = request.args.get('user1_id')
    user2_id = request.args.get('user2_id')

    user1 = User.query.filter_by(public_id=user1_id).first()
    user2 = User.query.filter_by(public_id=user2_id).first()

    user1_id = user1.id
    user2_id = user2.id

    print(user1_id)
    print(user2_id)

    thread = Thread.query.filter((Thread.user1_id == user1_id and Thread.user2_id == user2_id) or (
            Thread.user1_id == user2_id and Thread.user2_id == user1_id)).first()

    if thread is None:
        thread = Thread(user1_id, user2_id)

    args_data = request.get_json()

    message_data = args_data['message']
    print(message_data)

    format_date = datetime.strptime(message_data['timestamp'], '%d/%m/%Y %H:%M')

    sender = User.query.filter_by(public_id=message_data['sender_id']).first()

    thread.messages.append(Message(False, format_date, message_data['text'], sender.id))

    for i in thread.messages:
        print(i.to_dict())

    db.session.commit()

    return jsonify({'message': 'SUCCESS'})


@messages_blueprint.route("/threads/<int:thread_id>/messages", methods=['GET', 'DELETE'])
def thread_messages(thread_id):
    if request.method == 'GET':

        thread = Thread.query.filter_by(id=thread_id).first()

        if thread is None:
            return jsonify({'message': 'ERROR'})

        thread.messages[-1].is_read = True

        messages_dict = []

        for i in thread.messages:
            messages_dict.append(i.to_dict())

        print(messages_dict)

        db.session.commit()

        return jsonify(messages_dict)
    elif request.method == 'DELETE':

        thread = Thread.query.filter_by(id=thread_id).first()

        if thread is None:
            return jsonify({'message': 'ERROR'})

        message_id = request.args.get('message_id')

        del_message = Message.query.filter_by(id=message_id).first()

        if del_message is None:
            return jsonify({'message': 'ERROR'})

        db.session.delete(del_message)
        if not thread.messages:
            db.session.delete(thread)

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
