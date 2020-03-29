

import os

import markdown

from database import *

#from models.Amenity import Amenity
from models.Availability import Availability
from models.Image import Image
from models.Room import Room
from models.User import User

db.create_all()
#db.session.add(Room('house',1,2,3,True,'ok',True,True,True,0,0,'ok','ok',2,3,4))
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
    app.run(debug=True)
