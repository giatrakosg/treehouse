import sys
sys.path.append('../')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from ExplicitMF import Recommender, train_test_split
from tqdm import tqdm

from database import db
from models.User import User
from models.Room import Room
from models.Recommendation import Recommendation

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

reviews = pd.read_csv('../data/reviews_with_scores.csv',index_col=0)

users = reviews.reviewer_id.unique()
items = reviews.listing_id.unique()

n_users = users.shape[0]
n_items = items.shape[0]
ratings = np.zeros((n_users, n_items),dtype=np.float128)

reviews['uidx'] = reviews['reviewer_id'].apply(lambda x: np.where(users==x)[0][0])
reviews['iidx'] = reviews['listing_id'].apply(lambda x: np.where(items==x)[0][0])

for idx,row in reviews.iterrows():
    ratings[row[7],row[8]] = row[6]

mf = Recommender(n_epochs=5)
train, val = train_test_split(ratings)
mf.fit(train,val)

renters = User.query.filter_by(isHost=False,isAdmin=False).all()
rentidx = 0

for u in tqdm(range(253)):
    rat_u = mf.predict(train,u)
    top_5 = rat_u.argsort()[0:5]
    renterid = renters[rentidx].id
    rentidx+=1

    for num,ind in enumerate(top_5):
        idx = (reviews['iidx'] == ind).idxmax()
        listingid = reviews.iloc[idx]['listing_id']
        room = Room.query.filter_by(listingid=int(listingid)).first()
        if room:
            rec = Recommendation(rank=num,uid=renterid,roomid=room.id)
            db.session.add(rec)

db.session.commit()
