from database import db

"""////////  AVAILABILITY   ///////////////////               """


class Availability(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_from = db.Column(db.DateTime, nullable=False)
    date_to = db.Column(db.DateTime, nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)

    def __init__(self, date_from, date_to):
        self.date_from = date_from
        self.date_to = date_to

    def to_dict(self):
        r = {'date_from': self.date_from, 'date_to': self.date_to}
        return r


"""///////////////////////////////////////////////////////////"""
