from database import db
import enum

from models.Availability import Availability
from models.Image import Image
from models.Review import Review

"""////////  ROOM   ///////////////////               """


class RoomTypes(enum.Enum):
    private_room = 0
    shared_room = 1
    house = 2


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
    x_coordinate = db.Column(db.Float, nullable=False)
    y_coordinate = db.Column(db.Float, nullable=False)
    address = db.Column(db.String(50), nullable=False)
    transport_info = db.Column(db.String(100))
    persons_num = db.Column(db.Integer, nullable=False)
    standard_cost = db.Column(db.Float, nullable=False)
    add_persons_cost = db.Column(db.Float)
    reviews_score = db.Column(db.Float)
    title = db.Column(db.String(30), nullable=False)

    images = db.relationship('Image', backref='room', lazy=True)

    reviews = db.relationship('Review', backref='room', lazy=True)

    availabilities = db.relationship('Availability', backref='room', lazy=True)

    def __init__(self, rt, beds_num, baths_num, bedr_num, lounge, desc,
                 smoking_all, pets_all, events_all, wifi, ac, refrigerator, kitchen, tv, parking, elevator, x, y,
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
        self.x_coordinate = x
        self.y_coordinate = y
        self.address = address
        self.transport_info = tran_info
        self.persons_num = pers_num
        self.standard_cost = standard_cost
        self.add_persons_cost = add_prs_cost
        self.reviews_score = reviews_score
        self.title = title

    def to_dict_short(self):
        r = {'title': self.title,
             'Type': self.Type,
             'review_scores': self.reviews_score,
             'beds_number': self.beds_num,
             'cost_per_day': self.standard_cost,
             'image_src': self.images[0].source}

        return r


"""///////////////////////////////////////////////////////////"""
