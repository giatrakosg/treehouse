from database import db
from datetime import datetime, timedelta
import random

from models.Message import Message
from models.User import User
import string


class Thread(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    host_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    renter_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)

    messages = db.relationship('Message', backref='thread', lazy=True)

    def to_dict(self):
        messages = []
        d = {}

        for m in self.messages:
            messages.append(m.to_dict())

        d['messages'] = messages
        return d

    def get_random_messages(self):
        time = datetime.now()

        for x in range(10):
            text = random_sentence(10)

            self.messages.append(Message(False, time, text))

            time = time + timedelta(days=random.randint(2, 30))

    def to_dict_short(self):
        d = {'username': 'john', 'last_message': self.messages[-1].to_dict(), 'id': self.id}

        return d

    def destroy(self):
        for m in self.messages:
            db.session.delete(m)


def random_sentence(words_number):
    letters = string.ascii_letters

    sentence = ''

    for x in range(words_number):
        word = ''.join(random.choice(letters) for i in range(6))

        sentence = sentence + ' ' + word

    return sentence
