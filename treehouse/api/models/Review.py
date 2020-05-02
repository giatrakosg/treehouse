from database import db

"""////////  REVIEW   ///////////////////               """


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Float, nullable=False)
    title = db.Column(db.String(30), nullable=False)
    description = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)

    def __init__(self, score, title, description, user):
        self.rating = score
        self.description = description
        self.user_id = user
        self.title = title

    def to_dict(self):
        r = {'rating': self.rating,
             'title': self.title,
             'description': self.description,
             'user_id': self.user_id}
        return r


"""///////////////////////////////////////////////////////////"""
