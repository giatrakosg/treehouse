from database import *


"""////////////////AMENITY////////////////////////////////////"""


class Amenity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(20), primary_key=True)


room_has_amenities = db.Table('room_has_amenities',
                              db.Column('room_id', db.Integer, db.ForeignKey('room.id'), primary_key=True),
                              db.Column('amenity_id', db.Integer, db.ForeignKey('amenity.id'), primary_key=True),
                              )


"""///////////////////////////////////////////////////////////"""
