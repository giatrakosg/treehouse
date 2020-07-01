import sys
sys.path.append('../')

from database import db
from models.User import User
from models.Review import Review
from models.Room import Room, RoomTypes
from routes.Users import generate_password_hash
import pandas as pd
import random
import uuid
import re
import numpy as np
from tqdm import tqdm
import requests

def createUser(seen,rec):
    if rec['reviewer_id'] in seen:
        return
    pwd = generate_password_hash(rec['reviewer_name'])
    pid = str(uuid.uuid4())
    isHost = bool(random.getrandbits(1))

    user = User(public_id=pid,password=pwd,fname=rec['reviewer_name'],
    surname="Doe",uname=rec['reviewer_name']+str(rec['reviewer_id']),email=rec['reviewer_name']+'@hotmail.com',phone='69',isHost=isHost,isPending=False,
    avatar='https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80')

    db.session.add(user)
    seen.add(rec['reviewer_id'])

def createRoom(rec):
    if rec['room_type'] == 'Entire home/apt':
        rt = RoomTypes.house
    if rec['room_type'] == 'Private room':
        rt = RoomTypes.private_room
    if rec['room_type'] == 'Shared room':
        rt = RoomTypes.shared_room


    hosts = User.query.filter_by(isHost=True).all()
    ind = random.randrange(len(hosts))
    host = hosts[ind]

    lounge = bool(random.getrandbits(1))
    smoking = bool(random.getrandbits(1))
    pets = bool(random.getrandbits(1))
    events = bool(random.getrandbits(1))
    wifi = bool(random.getrandbits(1))
    ac = bool(random.getrandbits(1))
    refr = bool(random.getrandbits(1))
    kitch = bool(random.getrandbits(1))
    tv = bool(random.getrandbits(1))
    parking = bool(random.getrandbits(1))
    elev = bool(random.getrandbits(1))
    area = random.randrange(150)

    room = Room(rt=rt,beds_num=rec['beds'],baths_num=rec['bathrooms'],bedr_num=rec['bedrooms'],
    lounge=lounge,desc=rec['description'],smoking_all=smoking,pets_all=pets,events_all=events,
    wifi=wifi,ac=ac,refrigerator=refr,kitchen=kitch,tv=tv,parking=parking,elevator=elev,latitude=rec['latitude'],
    longitude=rec['longitude'],address=rec['street']+','+rec['city'],tran_info=rec['transit'],pers_num=rec['guests_included'],
    standard_cost=rec['price'],add_prs_cost=3,title=rec['name'],area=area,min_stay=rec['minimum_nights'],owner_id=host.id
    ,listing_id=rec['id'])
    db.session.add(room)

revpd = pd.read_csv('../data/reviews_less.csv',index_col=0)
roompd = pd.read_csv('../data/listings.csv')

# We remove the . thousand(separator) and the first char that is the dollar sign
roompd['price'] = roompd['price'].apply(lambda x: x.split()[0].replace(',', ''))
roompd['price'] = roompd['price'].str[1:].astype(np.float32)
roompd['guests_included'] = roompd['guests_included'].astype(np.int16)

tqdm.pandas()

seen = set([])

#for index, row in tqdm(revpd.iterrows(),total=revpd.shape[0]):
#    createUser(seen,row)
roompd['bathrooms'].fillna(0,inplace=True)
roompd['beds'].fillna(0,inplace=True)
roompd['bedrooms'].fillna(0,inplace=True)

revpd.progress_apply(lambda x : createUser(seen,x),axis=1)
db.session.commit()

roompd.progress_apply(lambda x : createRoom(x),axis=1)
db.session.commit()
