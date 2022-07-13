from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

#import os
#pip3 install pymysql
#app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI") 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from application import routes
