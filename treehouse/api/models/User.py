from database import db


"""////////  USER   ///////////////////               """

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String,nullable=False)
    name = db.Column(db.String,nullable=False)
    surname = db.Column(db.String,nullable=False)
    email = db.Column(db.String,nullable=False)
    phone = db.Column(db.String,nullable=False)
    avatar = db.Column(db.String,nullable=False)
    isAdmin = db.Column(db.Boolean,nullable=False)
    isHost = db.Column(db.Boolean,nullable=False)

    def __init__(self, id,password,name,surname,email,phone,avatar,isAdmin,isHost):
        self.id = id
        self.password = password
        self.name = name
        self.surname = surname
        self.email = email
        self.phone = phone
        self.avatar = avatar
        self.isAdmin = isAdmin
        self.isHost = isHost


"""///////////////////////////////////////////////////////////"""
