from flask import Flask, request, url_for, render_template, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

from models.student_table import *
from models.supportstaff_table import *

from __init__ import app


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/' #this works with @login_required decorator
login_manager.login_message = 'You need to log in with correct credentials before going to Home Page!'

## mapping the python flask object with the object in the actual model
@login_manager.user_loader
def load_user(user_id):
	staff_id = SupportStaff.query.get(user_id)
	student_id = Students.query.get(int(user_id))
	if student_id:
		return student_id
	else:
		return staff_id


@app.route('/')
def login():
	return render_template("login.html")


@app.route('/loggedin', methods = ['POST'])
def loggedin():
	id = request.form['id']
	password = request.form['password']

	student = Students.query.filter_by(id = id).first()
	staff = SupportStaff.query.filter_by(username = id).first()


	if not student and not staff:
		flash('User Not Found! Please contact the Exam Dept.')
		return redirect(url_for('login'))
	elif student:
		if student.password != password:
			flash('Invalid Credentials!')
			return redirect(url_for('login'))
		else:
			login_user(student)
			return redirect(url_for('home'))
	elif staff:
		if staff.password != password:
			flash('Invalid Credentials!')
			return redirect(url_for('login'))
		else:
			login_user(staff)
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
	return redirect(url_for('department.department_homepage', dept_name = current_user.dept))


# main function
if __name__ == '__main__':
	app.run(debug=True)