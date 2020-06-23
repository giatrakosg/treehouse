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

    def __init__(self, host_id, renter_id):
        self.host_id = host_id
        self.renter_id = renter_id

    def to_dict(self):
        d = {'last_message': self.messages[-1].to_dict()}

        return d

    def get_random_messages(self):
        time = datetime.now()

        for x in range(10):
            text = random_sentence(10)

            self.messages.append(Message(False, time, text, bool(random.getrandbits(1))))

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
