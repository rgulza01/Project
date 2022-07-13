from flask import Flask
from application import app, db
from application.models import *

@app.route("/")
def index():
	return "Bismillah"
