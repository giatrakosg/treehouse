
from database import db

"""////////  AVAILABILITY   ///////////////////               """


class Availability(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # date=
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)


"""///////////////////////////////////////////////////////////"""
