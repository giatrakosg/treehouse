from flask import Blueprint, jsonify, request
from database import db
from sqlalchemy import or_

from models.Thread import Thread
from models.Message import Message
from models.Room import Room
from models.User import User

from datetime import datetime, timedelta
import json

messages_blueprint = Blueprint('messages', __name__)


@messages_blueprint.route("/threads/thread/new_message", methods=['POST'])
def new_thread_message():
    sender_public_id = request.args.get('sender_public_id')
    receiver_public_id = request.args.get('receiver_public_id')
    room_id = request.args.get('room_id')

    print(sender_public_id)
    print(receiver_public_id)
    print(room_id)

    user1 = User.query.filter_by(public_id=sender_public_id).first()
    user2 = User.query.filter_by(public_id=receiver_public_id).first()

    user1_id = user1.id
    user2_id = user2.id

    print(user1_id)
    print(user2_id)
    print(room_id)

    thread = Thread.query.filter_by(user1_id=user1_id, user2_id=user2_id).first()
    if thread is None:
        thread = Thread.query.filter_by(user2_id=user1_id, user1_id=user2_id).first()

    if thread is None:
        thread = Thread(user1_id, user2_id)
        room = Room.query.filter_by(id=room_id).first()
        room.threads.append(thread)

    args_data = request.get_json()

    message_data = args_data['message']
    print(message_data)

    format_date = datetime.strptime(message_data['timestamp'], '%d/%m/%Y %H:%M')

    sender = User.query.filter_by(public_id=sender_public_id).first()

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


@messages_blueprint.route("/users/<public_user_id>/threads", methods=['GET'])
def get_user_threads(public_user_id):
    user = User.query.filter_by(public_id=public_user_id).first()

    if user is None:
        return jsonify({'message': 'SUCCESS'})

    threads = Thread.query.filter(or_(Thread.user1_id == user.id, Thread.user2_id == user.id)).all()
    threads_dict = []

    for t in threads:
        threads_dict.append(t.to_dict())
    return jsonify(threads_dict)


@messages_blueprint.route("/rooms/<int:room_id>/threads", methods=['GET'])
def get_room_threads(room_id):
    room = Room.query.filter_by(id=room_id).first()

    if room is None:
        return jsonify({'message': 'ERROR'})

    threads_dict = []
    threads = room.threads

    for t in threads:
        threads_dict.append(t.to_dict())

    return jsonify(threads_dict)
