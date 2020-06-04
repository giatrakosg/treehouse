from database import db


"""////////  USER   ///////////////////               """


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    isAdmin = db.Column(db.Boolean)
    isHost = db.Column(db.Boolean)
    isPending = db.Column(db.Boolean)
    uname = db.Column(db.String(32),unique=True)
    password = db.Column(db.String(80))
    fname = db.Column(db.String(32))
    surname = db.Column(db.String(32))
    email = db.Column(db.String(32))
    phone = db.Column(db.String(15))

    def __init__(self,public_id,isHost,uname,password,fname,surname,email,phone,isPending=True,isAdmin=False):
        #self.id = id
        self.public_id = public_id
        self.isAdmin = isAdmin
        self.isHost = isHost
        self.isPending = isPending
        self.uname = uname
        self.password = password
        self.fname = fname
        self.surname = surname
        self.email = email
        self.phone = phone
    def to_dict(self) :
        dict = {}
        dict['public_id'] = self.public_id
        dict['isAdmin'] = self.isAdmin
        dict['isHost'] = self.isHost
        dict['isPending'] = self.isPending
        dict['uname'] = self.uname
        dict['fname'] = self.fname
        dict['surname'] = self.surname
        dict['email'] = self.email
        dict['phone'] = self.phone
        return dict


"""///////////////////////////////////////////////////////////"""
