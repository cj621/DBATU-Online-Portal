from flask import Blueprint
from flask import Flask, request, url_for, render_template, redirect, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import datetime
from sqlalchemy import desc

dept_module = Blueprint('department', __name__)

from models.departmentnews_table import *


### New Post Creation ###
@dept_module.route('/new_post', methods=['GET', 'POST'])
@login_required
def new_post():
	id = datetime.now()
	dept = current_user.dept
	news_for = request.form['news_for']
	news = request.form['newsdetail']
	posted_by = current_user.name

	new_post = DepartmentNews(id=id, dept=dept, news_for=news_for, news=news, posted_by=posted_by)
	db.session.add(new_post)
	db.session.commit()

	if news_for == 'department':
		return redirect(url_for('department.department_homepage', dept_name = current_user.dept))
	else:
		return redirect(url_for('department.department_'+news_for, dept_name = current_user.dept))
	


###################################################################################
# All Departments #

@dept_module.route('/<dept_name>')
@login_required
def department_homepage(dept_name):
	news = DepartmentNews.query.filter_by(dept = current_user.dept, news_for = 'department').order_by(desc(DepartmentNews.id))
	return render_template("department_homepage.html", current_user = current_user, news = news)

@dept_module.route('/<dept_name>/first_year')
@login_required
def department_first_year(dept_name):
	news = DepartmentNews.query.filter_by(dept = current_user.dept, news_for = 'first_year').order_by(desc(DepartmentNews.id))
	return render_template("department_homepage.html", current_user = current_user, news = news)

@dept_module.route('/<dept_name>/second_year')
@login_required
def department_second_year(dept_name):
	news = DepartmentNews.query.filter_by(dept = current_user.dept, news_for = 'second_year').order_by(desc(DepartmentNews.id))
	return render_template("department_homepage.html", current_user = current_user, news = news)

@dept_module.route('/<dept_name>/third_year')
@login_required
def department_third_year(dept_name):
	news = DepartmentNews.query.filter_by(dept = current_user.dept, news_for = 'third_year').order_by(desc(DepartmentNews.id))
	return render_template("department_homepage.html", current_user = current_user, news = news)

@dept_module.route('/<dept_name>/final_year')
@login_required
def department_final_year(dept_name):
	news = DepartmentNews.query.filter_by(dept = current_user.dept, news_for = 'final_year').order_by(desc(DepartmentNews.id))
	return render_template("department_homepage.html", current_user = current_user, news = news)



########################################################################################
# University news

@dept_module.route('/university_news')
def university_news():
	return render_template("university_news.html", current_user = current_user)
