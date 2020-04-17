from database import db
from enum import Enum

from models.Availability import Availability
from models.Image import Image
from models.Review import Review

"""////////  ROOM   ///////////////////               """


class RoomTypes(str, Enum):
    private_room = 'private room'
    shared_room = 'shared room'
    house = 'house'


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
    wireless_internet = db.Column(db.Boolean, nullable=False)
    air_condition = db.Column(db.Boolean, nullable=False)
    refrigerator = db.Column(db.Boolean, nullable=False)
    kitchen = db.Column(db.Boolean, nullable=False)
    tv = db.Column(db.Boolean, nullable=False)
    parking = db.Column(db.Boolean, nullable=False)
    elevator = db.Column(db.Boolean, nullable=False)
    lat_coordinate = db.Column(db.Float, nullable=False)
    long_coordinate = db.Column(db.Float, nullable=False)
    address = db.Column(db.String(50), nullable=False)
    transport_info = db.Column(db.String(100))
    persons_num = db.Column(db.Integer, nullable=False)
    standard_cost = db.Column(db.Float, nullable=False)
    add_persons_cost = db.Column(db.Float)
    rating = db.Column(db.Float)
    title = db.Column(db.String(30), nullable=False)

    images = db.relationship('Image', backref='room', lazy=True)

    reviews = db.relationship('Review', backref='room', lazy=True)

    availabilities = db.relationship('Availability', backref='room', lazy=True)

    def __init__(self, rt, beds_num, baths_num, bedr_num, lounge, desc,
                 smoking_all, pets_all, events_all, wifi, ac, refrigerator, kitchen, tv,
                 parking, elevator, latitude, longitude,
                 address, tran_info, pers_num,
                 standard_cost, add_prs_cost, reviews_score, title):
        self.Type = rt
        self.beds_num = beds_num
        self.baths_num = baths_num
        self.bedrooms_num = bedr_num
        self.lounge = lounge
        self.description = desc
        self.smocking_allowed = smoking_all
        self.pets_allowed = pets_all
        self.events_allowed = events_all
        self.wireless_internet = wifi
        self.air_condition = ac
        self.refrigerator = refrigerator
        self.kitchen = kitchen
        self.tv = tv
        self.parking = parking
        self.elevator = elevator
        self.lat_coordinate = latitude
        self.long_coordinate = longitude
        self.address = address
        self.transport_info = tran_info
        self.persons_num = pers_num
        self.standard_cost = standard_cost
        self.add_persons_cost = add_prs_cost
        self.rating = reviews_score
        self.title = title

    def to_dict_short(self):
        r = {'type': self.Type,
             'beds_number': self.beds_num,
             'wireless_internet': self.wireless_internet,
             'air_condition': self.air_condition,
             'refrigerator': self.refrigerator,
             'kitchen': self.kitchen,
             'tv': self.tv,
             'parking': self.parking,
             'elevator': self.elevator,
             'title': self.title,
             'persons_number': self.persons_num,
             'rating': self.rating,
             'cost_per_day': self.standard_cost,
             'image_src': self.images[0].source}
        return r


"""///////////////////////////////////////////////////////////"""
