import os

import markdown

from database import *
from flask_cors import CORS

from models.Reservation import Reservation
from models.Image import Image
from models.Room import Room
from models.User import User

from routes.Rooms import rooms_blueprint

cors = CORS(app)

app.register_blueprint(rooms_blueprint)

db.create_all()

db.session.commit()

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message' : 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = User.query.filter_by(public_id=data['public_id']).first()
        except:
            return jsonify({'message' : 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated



@app.route('/', methods=['GET'])
def hello():
    output = ''
    # Open the README file
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:
        # Read the content of the file
        content = markdown_file.read()

        # Convert to HTML
        output += markdown.markdown(content)
    return output

@app.route('/login',methods=['GET'])
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    user = User.query.filter_by(uname=auth.username).first()

    if not user:
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    if check_password_hash(user.password, auth.password):
        token = jwt.encode({'public_id' : user.public_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=90)}, app.config['SECRET_KEY'])

        return jsonify({'token' : token.decode('UTF-8')})

    return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

@app.route('/user', methods=['POST'])
def addUserRequest():
    data = request.get_json()
    print(data,file=sys.stderr)
    hashed_password = generate_password_hash(data['password'], method='sha256')

    uName = User.query.filter_by(uname=data['uname']).all()
    if len(uName) > 0 :
        return jsonify({'message' : 'User already exists!'}),400
    uEmail = User.query.filter_by(email=data['email']).all()
    if len(uEmail) > 0 :
        return jsonify({'message' : 'Email already exists!'}),400

    new_user = User(
    public_id=str(uuid.uuid4()),
    uname=data['uname'],
    password=hashed_password,
    fname=data['fname'],
    surname=data['surname'],
    email=data['email'],
    phone=data['phone'],
    isHost=data['isHost'],
    isPending=data['isHost']
    )

    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message' : 'New user created!'})


@app.route('/user/pending', methods=['GET'])
@token_required
def showPendingUsers(current_user):

    if not current_user.isAdmin:
        return jsonify({'message' : 'Cannot perform that function!'})

    users = User.query.all()

    output = []

    for user in users:
        if user.isPending is False:
            continue
        user_data = {}
        user_data['public_id'] = user.public_id
        user_data['name'] = user.uname
        user_data['email'] = user.email
        user_data['first_name'] = user.fname
        user_data['last_name'] = user.surname

        output.append(user_data)

    return jsonify({'users' : output})
@app.route('/user/pending/<user_public_id>', methods=['PUT'])
@token_required
def acceptUser(current_user, user_public_id):
    if not current_user.admin:
        return jsonify({'message' : 'Cannot perform that function!'})

    user = User.query.filter_by(public_id=user_public_id).first()

    if not user:
        return jsonify({'message' : 'No user found!'})
    if user.pending == False :
        return jsonify({'message' : 'User not pending !'})


    print(user.id)
    sem.acquire()
    sqlAddID = "INSERT INTO User VALUES ({})".format(user.id)
    cursor = dbItems.cursor()
    cursor.execute(sqlAddID)
    dbItems.commit()
    cursor.close()
    sem.release()

    sqlCreateSeller = "INSERT INTO Seller VALUES (NULL,0,{},0)".format(user.id)
    sem.acquire()
    cursor = dbItems.cursor()
    cursor.execute(sqlCreateSeller)
    dbItems.commit()
    cursor.close()
    sem.release()

    sqlCreateBidder = "INSERT INTO Bidder VALUES (NULL,0,'Adanon 7',{},0)".format(
    user.id)
    sem.acquire()
    cursor = dbItems.cursor()
    cursor.execute(sqlCreateBidder)
    dbItems.commit()
    cursor.close()
    sem.release()

    user.pending = False
    dbUsers.session.commit()

    return jsonify({'message' : 'The user has been accepted!'}),200


@app.route('/user/<public_id>', methods=['PUT'])
@token_required
def promote_user(current_user, public_id):
    if not current_user.admin:
        return jsonify({'message' : 'Cannot perform that function!'})

    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({'message' : 'No user found!'})

    user.admin = True
    dbUsers.session.commit()

    return jsonify({'message' : 'The user has been promoted!'})

@app.route('/user/<public_id>', methods=['DELETE'])
@token_required
def delete_user(current_user, public_id):
    if not current_user.admin:
        return jsonify({'message' : 'Cannot perform that function!'})

    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({'message' : 'No user found!'})

    dbUsers.session.delete(user)
    dbUsers.session.commit()

    return jsonify({'message' : 'The user has been deleted!'})



if __name__ == '__main__':
    manager.run()
