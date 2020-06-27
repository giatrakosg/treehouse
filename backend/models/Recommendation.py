from database import db

from models.User import User
from models.Room import Room

class Recommendation(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    rank = db.Column(db.Integer)
    uid = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    roomid = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)
    def __init__(self,rank,uid,roomid):
        self.rank = rank
        self.uid = uid
        self.roomid = roomid
    def to_dict(self):
        return {'id':self.id ,'rank':self.rank, 'uid':self.uid, 'roomid':self.roomid}
