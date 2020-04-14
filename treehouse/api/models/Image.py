"""////////////////////////////IMAGE///////////////////////////////"""
from database import db


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(500))
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)

    def __init__(self, source, room):
        self.source = source
        self.room_id = room


"""///////////////////////////////////////////////////////////"""
