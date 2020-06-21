from enum import Enum

from database import db

from models.User import User

"""////////  AVAILABILITY   ///////////////////"""
class Status(Enum):
    not_available = 0
    rented = 1

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_from = db.Column(db.DateTime, nullable=False)
    date_to = db.Column(db.DateTime)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)
    status = db.Column(db.Enum(Status), nullable=False)
    renter_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

    def __init__(self, date_from, date_to, status):
        self.date_from = date_from
        self.date_to = date_to
        self.status = status

    def to_dict(self):
        r = {'date_from': self.date_from, 'date_to': self.date_to, 'status': self.status.value}
        return r


"""///////////////////////////////////////////////////////////"""
