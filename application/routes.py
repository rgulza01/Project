from flask import Flask, url_for, render_template
from application import app, db
from application.models import *

#templates provided by : copyright © Design template adopted from Gurupreeth Singh
#to also mention in the ackowledgements part of README.md
@app.route("/")
def index():
	return render_template('home.html')

@app.route("/login")
def login():
	return render_template('login.html')

@app.route("/register")
def register():
	return render_template('register.html')

@app.route("/dashboard")
def dashboard():
	return render_template('dashboard.html')

@app.route("/addnewuser")
def addnewuser():
	return render_template('addnewuser.html')

@app.route("/singleuser")
def singleuserprofile():
	return render_template('singleuser.html')

@app.route("/update")
def update():
	return render_template('updateuser.html')

@app.route("/logout")
def logout():
	return render_template('home.html')