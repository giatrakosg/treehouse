from database import db
from datetime import datetime, timedelta
import random

from models.Message import Message
from models.User import User
import string


class Thread(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user1_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user2_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)

    messages = db.relationship('Message', backref='thread', lazy=True)

    def __init__(self, user1_id, user2_id):
        self.user1_id = user1_id
        self.user2_id = user2_id

    def to_dict(self):
        user1 = User.query.filter_by(id=self.user1_id).first()
        user2 = User.query.filter_by(id=self.user2_id).first()

        d = {'Id': self.id, 'last_message': self.messages[-1].to_dict(),
             'profile': 'https://cdn.vuetifyjs.com/images/lists/1.jpg', 'user1_public_id': user1.public_id,
             'user2_public_id': user2.public_id}

        return d

    def get_random_messages(self):
        time = datetime.now()

        for x in range(10):
            text = random_sentence(10)

            self.messages.append(Message(False, time, text, random.randint(1, 2) * 2))

            time = time + timedelta(days=random.randint(2, 30))

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
