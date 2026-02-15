from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
import os
# this part was coded to make database configuration
current_path = os.path.dirname(__file__)
final_path = os.path.join( current_path , "app.db" )
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + final_path
db = SQLAlchemy(app)





from . import models
from . import routes


