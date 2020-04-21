from database import db


"""////////  USER   ///////////////////               """


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    def __init__(self, id):
        self.id = id


"""///////////////////////////////////////////////////////////"""
