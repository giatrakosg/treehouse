from database import db
from enum import Enum
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime

from models.Reservation import Reservation
from models.Image import Image
from models.Review import Review

"""////////  ROOM   ///////////////////               """


class RoomTypes(str, Enum):
    private_room = 'private room'
    shared_room = 'shared room'
    house = 'house'


class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Enum(RoomTypes))
    beds_num = db.Column(db.Integer, nullable=False)
    baths_num = db.Column(db.Integer, nullable=False)
    bedrooms_num = db.Column(db.Integer, nullable=False)
    lounge = db.Column(db.Boolean, nullable=False)
    description = db.Column(db.Text)
    smoking_allowed = db.Column(db.Boolean, nullable=False)
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
    area = db.Column(db.Float, nullable=False)
    min_stay = db.Column(db.Integer, nullable=False)

    images = db.relationship('Image', backref='room', lazy=True)

    reviews = db.relationship('Review', backref='room', lazy=True)

    reservations = db.relationship('Reservation', backref='room', lazy=True)

    @hybrid_property
    def rating(self):

        r_sum = 0
        reviews_num = len(self.reviews)

        for r in self.reviews:
            r_sum = r_sum + r.rating

        return r_sum / reviews_num

    def __init__(self, rt, beds_num, baths_num, bedr_num, lounge, desc,
                 smoking_all, pets_all, events_all, wifi, ac, refrigerator, kitchen, tv,
                 parking, elevator, latitude, longitude,
                 address, tran_info, pers_num,
                 standard_cost, add_prs_cost, title, area, min_stay):
        self.type = rt
        self.beds_num = beds_num
        self.baths_num = baths_num
        self.bedrooms_num = bedr_num
        self.lounge = lounge
        self.description = desc
        self.smoking_allowed = smoking_all
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
        self.title = title
        self.area = area
        self.min_stay = min_stay

    def to_dict_all(self):

        images = []
        reviews = []

        for i in self.reviews:
            review_dict = i.to_dict()
            reviews.append(review_dict)

        for i in self.images:
            image_dict = i.to_dict()
            images.append(image_dict)

        r = {
            'type': self.type,
            'beds_number': self.beds_num,
            'baths_number': self.baths_num,
            'lounge': self.lounge,
            'description': self.description,
            'wireless_internet': self.wireless_internet,
            'air_condition': self.air_condition,
            'refrigerator': self.refrigerator,
            'kitchen': self.kitchen,
            'tv': self.tv,
            'parking': self.parking,
            'elevator': self.elevator,
            'location': [self.lat_coordinate, self.long_coordinate],
            'smoking_allowed': self.smoking_allowed,
            'pets_allowed': self.pets_allowed,
            'events_allowed': self.events_allowed,
            'min_stay': self.min_stay,
            'area': self.area,
            'address': self.address,
            'transport_info': self.transport_info,
            'standard_cost': self.standard_cost,
            'add_persons_cost': self.add_persons_cost,
            'title': self.title,
            'persons_number': self.persons_num,
            'rating': self.rating,
            'cost_per_day': self.standard_cost,
            'images': images,
            'bedrooms_number': self.bedrooms_num,
            'reviews': reviews,
            'reviews_num': len(self.reviews)

        }

        reservations = []
        for date_range in self.reservations:
            reservations.append(date_range.to_dict())

        r['reservations'] = reservations
        return r

    def to_dict_host_short(self):
        r = {'title': self.title,
             'cost_per_day': self.standard_cost,
             'rating': self.rating,
             'address': self.address,
             'reviews_number': len(self.reviews),
             'location': [self.lat_coordinate, self.long_coordinate],
             }

        if len(self.images) == 0:
            r['thumbnail'] = ''
        else:
            r['thumbnail'] = self.images[0].source

        return r

    def to_dict_short(self):
        r = {'id': self.id,
             'type': self.type,
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
             'reviews_num': len(self.reviews)}

        if len(self.images) == 0:
            r['image_src'] = ''
        else:
            r['image_src'] = self.images[0].source
            return r

        return r

    def update(self, data):

        self.type = RoomTypes(data['type'])
        self.beds_num = data['beds_num']
        self.baths_num = data['baths_num']
        self.bedrooms_num = data['bedrooms_num']
        self.lounge = data['lounge']
        self.description = data['description']
        self.smoking_allowed = data['smoking_allowed']
        self.pets_allowed = data['pets_allowed']
        self.events_allowed = data['events_allowed']
        self.wireless_internet = data['wireless_internet']
        self.air_condition = data['air_condition']
        self.refrigerator = data['refrigerator']
        self.kitchen = data['kitchen']
        self.tv = data['tv']
        self.parking = data['parking']
        self.elevator = data['elevator']
        self.lat_coordinate = data['location'][0]
        self.long_coordinate = data['location'][1]
        self.address = data['address']
        self.transport_info = data['transport_info']
        self.persons_num = data['persons_num']
        self.standard_cost = data['cost_per_day']
        self.add_persons_cost = data['add_persons_cost']
        self.title = data['title']
        self.area = data['area']
        self.min_stay = data['min_stay']

        reservations = data['reservations']

        for a in self.reservations:
            db.session.delete(a)

        for a in reservations:
            d_from = datetime.strptime(a['date_from'], '%Y-%m-%d')
            d_to = datetime.strptime(a['date_to'], '%Y-%m-%d')

            self.reservations.append(Reservation(d_from, d_to))

        db.session.commit()

    """///////////////////////////////////////////////////////////"""
