from flask import Blueprint
from flask import Flask, request, url_for, render_template, redirect, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import datetime
from sqlalchemy import desc

dept_module = Blueprint('department', __name__)

from models.departmentnews_table import *

### New Post Creation ###
@dept_module.route('/new_post', methods=['POST'])
@login_required
def new_post():
	id = datetime.now()
	dept = current_user.dept
	news_for = request.form['news_for']
	news = request.form['newsdetail']
	posted_by = current_user.name

	new_dept_post = DepartmentNews(id=id, dept=dept, news_for=news_for, news=news, posted_by=posted_by)
	db.session.add(new_dept_post)
	db.session.commit()

	if news_for == 'department':
		return redirect(url_for('department.department_homepage', dept_name = current_user.dept))
	else:
		return redirect(url_for('department.department_year', dept_name = current_user.dept, year = news_for))
	

# All Departments #

@dept_module.route('/<dept_name>')
@login_required
def department_homepage(dept_name):
	news = DepartmentNews.query.filter_by(dept = current_user.dept, news_for = 'department').order_by(desc(DepartmentNews.id))
	return render_template("department_homepage.html", current_user = current_user, news = news)

@dept_module.route('/<dept_name>/<year>')
@login_required
def department_year(dept_name, year):
	news = DepartmentNews.query.filter_by(dept = current_user.dept, news_for = year).order_by(desc(DepartmentNews.id))
	return render_template("department_homepage.html", current_user = current_user, news = news)