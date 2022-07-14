import email
from flask import Flask, url_for, render_template, redirect, request, flash
from application import app, db
from application.models import UserForm, User


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
			#checks if email is in database and if it is not, I add the user's info in the database
			user = User.query.filter_by(email=form.email_box.data).first()
			if user is None:
				user = User(name=form.name_box.data, email=form.email_box.data)
				db.session.add(user)
				db.session.commit()
				flash(f'Thank you for joining our gluten free community {form.name_box.data}! You should recieve a confirmation email soon', 'success')
				return redirect(url_for('register')) 
			elif(len(form.email_box.data) < 3):
				flash(f'Email invalid', 'error')
				return redirect(url_for('register'))
			else:
				flash(f'Your email address has already been used. Try logging in or use a different email address', 'error')
				return redirect(url_for('register'))
	return render_template('register2.html', form = form)

@app.route("/dashboard")
def dashboard():
	list_users = User.query.all()
	return render_template('dashboard.html', list_users_in_html=list_users)

@app.route("/login")
def login():
	return render_template('login.html')


# I will change this into add new post 
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

#----------------Custom error page----------------
@app.errorhandler(404)
def pageNotFound(error_parameter):
    return render_template('404.html'), 404

@app.errorhandler(500)
def serverError(error_parameter):
    return render_template('500.html'), 500