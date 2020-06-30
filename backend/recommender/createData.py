import sys
sys.path.append('../')

from database import db
from models.User import User
from models.Review import Review
from models.Room import Room
from routes.Users import generate_password_hash
import pandas as pd
import random
import uuid
from tqdm import tqdm

def createUser(seen,rec):
    if rec['reviewer_id'] in seen:
        return
    pwd = generate_password_hash(rec['reviewer_name'])
    pid = str(uuid.uuid4())
    user = User(public_id=pid,password=pwd,fname=rec['reviewer_name'],
    surname="Doe",uname=rec['reviewer_name']+str(rec['reviewer_id']),email=rec['reviewer_name']+'@hotmail.com',phone='69',isHost=False,isPending=False)
    db.session.add(user)
    seen.add(rec['reviewer_id'])

def createRoom(rec):
    room = Room()

revpd = pd.read_csv('../data/reviews_less.csv',index_col=0)
roompd = pd.read_csv('../data/listings.csv',index_col='id')

tqdm.pandas()

print(revpd.head())

seen = set([])

#for index, row in tqdm(revpd.iterrows(),total=revpd.shape[0]):
#    createUser(seen,row)
revpd.progress_apply(lambda x : createUser(seen,x),axis=1)
db.session.commit()
