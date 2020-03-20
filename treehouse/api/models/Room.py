from database import db
import enum


from .Amenity import room_has_amenities
from .Availability import Availability
from .Image import Image


"""////////  ROOM   ///////////////////               """


class RoomTypes(enum.Enum):
    private_room = 1
    shared_room = 2
    house = 3


class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Type = db.Column(db.Enum(RoomTypes))
    beds_num = db.Column(db.Integer, nullable=False)
    baths_num = db.Column(db.Integer, nullable=False)
    bedrooms_num = db.Column(db.Integer, nullable=False)
    lounge = db.Column(db.Boolean, nullable=False)
    description = db.Column(db.Text)
    smocking_allowed = db.Column(db.Boolean, nullable=False)
    pets_allowed = db.Column(db.Boolean, nullable=False)
    events_allowed = db.Column(db.Boolean, nullable=False)
    x_coordinate = db.Column(db.Float, nullable=False)
    y_coordinate = db.Column(db.Float, nullable=False)
    address = db.Column(db.String(50), nullable=False)
    transport_info = db.Column(db.String(100))
    persons_num = db.Column(db.Integer, nullable=False)
    standard_cost = db.Column(db.Float, nullable=False)
    add_persons_cost = db.Column(db.Float)

    images = db.relationship('Image', backref='room', lazy=True)

    amenities = db.relationship('Amenity', secondary=room_has_amenities, lazy='subquery',
                                backref=db.backref('rooms', lazy=True))
    availabilities = db.relationship('Availability', backref='room', lazy=True)

    def __init__(self, rt, beds_num, baths_num, bedr_num, lounge, desc,
                 smoc_all, pets_all, events_all, x, y, address, tran_info, pers_num,
                 standr_cost, add_prs_cost):
        self.Type = rt
        self.beds_num = beds_num
        self.baths_num = baths_num
        self.bedrooms_num = bedr_num
        self.lounge = lounge
        self.description = desc
        self.smocking_allowed = smoc_all
        self.pets_allowed = pets_all
        self.events_allowed = events_all
        self.x_coordinate = x
        self.y_coordinate = y
        self.address = address
        self.transport_info = tran_info
        self.persons_num = pers_num
        self.standard_cost = standr_cost
        self.add_persons_cost = add_prs_cost


"""///////////////////////////////////////////////////////////"""
