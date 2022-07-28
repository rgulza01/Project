from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

# ---------------set up to run on local machine---------------
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SECRET_KEY'] = 'DUMMY_FOR_TESTING'

#---------------set up to run on Jenkins---------------
# app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI']=f"mysql+pymysql://radiagulzan@db-relationship-practice-mysql:{os.getenv('DATABASE_PASSWORD')}@{os.getenv('SERVER_NAME')}:3306/project_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from application import routes
