from flask import Flask, url_for, render_template
from application import app, db
from application.models import *

@app.route("/")
def index():
	return render_template('layout.html')
