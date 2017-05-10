from flask import Flask, request, url_for, render_template, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

from db import *

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/' #this works with @login_required decorator
login_manager.login_message = 'You need to log in with correct credentials before going to Home Page!'

## mapping the python flask object with the object in the actual model
@login_manager.user_loader
def load_user(user_id):
	return Students.query.get(int(user_id))


@app.route('/')
def login():
	return render_template("login.html")


@app.route('/loggedin', methods = ['POST'])
def loggedin():
	id = request.form['id']
	password = request.form['password']

	student = Students.query.filter_by(id = id).first()

	if not student:
		flash('User Not Found! Please contact the Exam Dept.')
		return redirect(url_for('login'))
	elif student.password != password:
		flash('Invalid Credentials!')
		return redirect(url_for('login'))
		

	login_user(student)
	return redirect(url_for('home'))


@app.route('/logout')
@login_required
def logout():
	logout_user()
	flash('Successfully Logged Out!')
	return redirect(url_for('login'))

@app.route('/home')
@login_required
def home():
	return render_template("student_home.html", student_name = current_user.name)


if __name__ == '__main__':
	app.run(debug=True)