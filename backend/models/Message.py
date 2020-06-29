from database import db

from models.User import User


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    thread_id = db.Column(db.Integer, db.ForeignKey('thread.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    text = db.Column(db.String(100), nullable=False)
    is_read = db.Column(db.Boolean, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

    def __init__(self, is_read, timestamp, text, sender_id):
        self.is_read = is_read
        self.timestamp = timestamp
        self.text = text
        self.user_id = sender_id

    def to_dict(self):
        user = User.query.filter_by(id=self.user_id).first()

        d = {
            'text': self.text,
            'timestamp': self.timestamp,
            'is_read': self.is_read,
            'sender': user.uname,
            'sender_public_id': user.public_id,
            'id': self.id,
            'thread_id': self.thread_id
        }
        return d
