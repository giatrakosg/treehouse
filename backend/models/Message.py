from database import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    thread_id = db.Column(db.Integer, db.ForeignKey('thread.id'), nullable=False)
    # sender  =user_id
    text = db.Column(db.String(100), nullable=False)
    is_read = db.Column(db.Boolean, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

    def __init__(self, is_read, timestamp, text):
        self.is_read = is_read
        self.timestamp = timestamp
        self.text = text

    def to_dict(self):
        d = {
            'text': self.text,
            'timestamp': self.timestamp,
            'is_read': self.is_read,
            'sender': 'John_test',
            'id': self.id
        }
        return d
