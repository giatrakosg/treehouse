from database import db


"""////////  USER   ///////////////////               """


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isAdmin = db.Column(db.Boolean)
    isHost = db.Column(db.Boolean)

    def __init__(self, id):
        self.id = id


"""///////////////////////////////////////////////////////////"""
