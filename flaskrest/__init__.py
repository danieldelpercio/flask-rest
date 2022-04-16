import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# init app
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

# db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(
    basedir, 'db.sqlite'
    )
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# init database
db = SQLAlchemy(app)

# init marshmallow
ma = Marshmallow(app)


import flaskrest.product
import flaskrest.weather


@app.route('/')
def index():
    return "<p>Index</p>"
