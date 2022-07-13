from flask import Flask, url_for, render_template, redirect, request, flash
from application import app, db
from application.models import UserForm


#Teal coloured templates provided by : copyright © Design template adopted from Gurupreeth Singh
#to also mention in the ackowledgements part of README.md
@app.route("/")
def index():
	return render_template('home.html')

@app.route('/register', methods=["POST", "GET"])
def register():
	form = UserForm()
	
	if request.method == 'POST':
		if form.validate_on_submit():
			flash(f'Thank you for joining our gluten free community {form.name_box.data}! You should recieve a confirmation email soon', 'success')
			return redirect(url_for('register')) 

	return render_template('register2.html', form = form)

@app.route("/login")
def login():
	return render_template('login.html')

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