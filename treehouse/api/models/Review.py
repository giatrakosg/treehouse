from database import db

"""////////  REVIEW   ///////////////////               """


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    review_score = db.Column(db.Float, nullable=False)
    title = db.Column(db.String(30), nullable=False)
    description = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)

    def __init__(self, score, title, description, user, room):
        self.review_score = score
        self.description = description
        self.user_id = user
        self.title = title
        self.room_id = room

    def to_dict(self):
        r = {'review_score': self.review_score,
             'title': self.title,
             'description': self.description,
             'user_id': self.user_id,
             'room_id': self.room_id}
        return r


"""///////////////////////////////////////////////////////////"""
