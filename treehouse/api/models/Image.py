"""////////////////////////////IMAGE///////////////////////////////"""
from database import db


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.Text, primary_key=True)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)


"""///////////////////////////////////////////////////////////"""
