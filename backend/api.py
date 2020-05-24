import os

import markdown

from database import *
from flask_cors import CORS

from models.Reservation import Reservation
from models.Image import Image
from models.Room import Room
from models.User import User

from routes.Rooms import rooms_blueprint
from routes.Users import  users_blueprint


app.register_blueprint(rooms_blueprint)
app.register_blueprint(users_blueprint)

db.create_all()

db.session.commit()

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

if __name__ == '__main__':
    manager.run()
