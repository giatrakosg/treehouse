"""////////////////////////////IMAGE///////////////////////////////"""
from database import db


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(500))
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)

    def __init__(self, source):
        self.source = source

    def to_dict(self):
        r = {
            'src': self.source
        }

        return r


"""///////////////////////////////////////////////////////////"""
