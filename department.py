from flask import Blueprint
from flask import Flask, request, url_for, render_template, redirect, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import datetime
from sqlalchemy import desc

dept_module = Blueprint('department', __name__)

from models.departmentnews_table import *


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
		return redirect(url_for('department.'+current_user.dept))
	else:
		return redirect(url_for('department.'+current_user.dept+'_'+news_for))
	


###################################################################################
# Computer Department #

@dept_module.route('/Computer')
@login_required
def Computer():
	news = DepartmentNews.query.filter_by(dept = current_user.dept, news_for = 'department').order_by(desc(DepartmentNews.id))
	return render_template("computer_homepage.html", current_user = current_user, news = news)

@dept_module.route('/Computer/first_year')
@login_required
def Computer_first_year():
	news = DepartmentNews.query.filter_by(dept = current_user.dept, news_for = 'first_year').order_by(desc(DepartmentNews.id))
	return render_template("computer_homepage.html", current_user = current_user, news = news)

@dept_module.route('/Computer/second_year')
@login_required
def Computer_second_year():
	news = DepartmentNews.query.filter_by(dept = current_user.dept, news_for = 'second_year').order_by(desc(DepartmentNews.id))
	return render_template("computer_homepage.html", current_user = current_user, news = news)

@dept_module.route('/Computer/third_year')
@login_required
def Computer_third_year():
	news = DepartmentNews.query.filter_by(dept = current_user.dept, news_for = 'third_year').order_by(desc(DepartmentNews.id))
	return render_template("computer_homepage.html", current_user = current_user, news = news)

@dept_module.route('/Computer/final_year')
@login_required
def Computer_final_year():
	news = DepartmentNews.query.filter_by(dept = current_user.dept, news_for = 'final_year').order_by(desc(DepartmentNews.id))
	return render_template("computer_homepage.html", scurrent_user = current_user, news = news)


#########################################################################
# Chemical Department #

@dept_module.route('/Chemical')
@login_required
def Chemical():
	news = DepartmentNews.query.filter_by(dept = current_user.dept, news_for = 'department').order_by(desc(DepartmentNews.id))
	return render_template("chemical_homepage.html", current_user = current_user, news = news)

@dept_module.route('/Chemical/first_year')
@login_required
def Chemical_first_year():
	news = DepartmentNews.query.filter_by(dept = current_user.dept, news_for = 'first_year').order_by(desc(DepartmentNews.id))
	return render_template("chemical_homepage.html", current_user = current_user, news = news)

@dept_module.route('/Chemical/second_year')
@login_required
def Chemical_second_year():
	news = DepartmentNews.query.filter_by(dept = current_user.dept, news_for = 'second_year').order_by(desc(DepartmentNews.id))
	return render_template("chemical_homepage.html", current_user = current_user, news = news)

@dept_module.route('/Chemical/third_year')
@login_required
def Chemical_third_year():
	news = DepartmentNews.query.filter_by(dept = current_user.dept, news_for = 'third_year').order_by(desc(DepartmentNews.id))
	return render_template("chemical_homepage.html", current_user = current_user, news = news)

@dept_module.route('/Chemical/final_year')
@login_required
def Chemical_final_year():
	news = DepartmentNews.query.filter_by(dept = current_user.dept, news_for = 'final_year').order_by(desc(DepartmentNews.id))
	return render_template("chemical_homepage.html", current_user = current_user, news = news)


#########################################################################
# IT Department #

@dept_module.route('/IT')
@login_required
def IT():
	news = DepartmentNews.query.filter_by(dept = current_user.dept, news_for = 'department').order_by(desc(DepartmentNews.id))
	return render_template("it_homepage.html", current_user = current_user, news = news)

@dept_module.route('/IT/first_year')
@login_required
def IT_first_year():
	news = DepartmentNews.query.filter_by(dept = current_user.dept, news_for = 'first_year').order_by(desc(DepartmentNews.id))
	return render_template("it_homepage.html", current_user = current_user, news = news)

@dept_module.route('/IT/second_year')
@login_required
def IT_second_year():
	news = DepartmentNews.query.filter_by(dept = current_user.dept, news_for = 'second_year').order_by(desc(DepartmentNews.id))
	return render_template("it_homepage.html", current_user = current_user, news = news)

@dept_module.route('/IT/third_year')
@login_required
def IT_third_year():
	news = DepartmentNews.query.filter_by(dept = current_user.dept, news_for = 'third_year').order_by(desc(DepartmentNews.id))
	return render_template("it_homepage.html", current_user = current_user, news = news)

@dept_module.route('/IT/final_year')
@login_required
def IT_final_year():
	news = DepartmentNews.query.filter_by(dept = current_user.dept, news_for = 'final_year').order_by(desc(DepartmentNews.id))
	return render_template("it_homepage.html", current_user = current_user, news = news)


########################################################################################
# PetroChemical Department

@dept_module.route('/PetroChemical')
@login_required
def PetroChemical():
	news = DepartmentNews.query.filter_by(dept = current_user.dept, news_for = 'department').order_by(desc(DepartmentNews.id))
	return render_template("petrochemical_homepage.html", current_user = current_user, news = news)

@dept_module.route('/PetroChemical/first_year')
@login_required
def PetroChemical_first_year():
	news = DepartmentNews.query.filter_by(dept = current_user.dept, news_for = 'first_year').order_by(desc(DepartmentNews.id))
	return render_template("petrochemical_homepage.html", current_user = current_user, news = news)

@dept_module.route('/PetroChemical/second_year')
@login_required
def PetroChemical_second_year():
	news = DepartmentNews.query.filter_by(dept = current_user.dept, news_for = 'second_year').order_by(desc(DepartmentNews.id))
	return render_template("petrochemical_homepage.html", current_user = current_user, news = news)

@dept_module.route('/PetroChemical/third_year')
@login_required
def CPetroChemical_third_year():
	news = DepartmentNews.query.filter_by(dept = current_user.dept, news_for = 'third_year').order_by(desc(DepartmentNews.id))
	return render_template("petrochemical_homepage.html", current_user = current_user, news = news)

@dept_module.route('/PetroChemical/final_year')
@login_required
def PetroChemical_final_year():
	news = DepartmentNews.query.filter_by(dept = current_user.dept, news_for = 'final_year').order_by(desc(DepartmentNews.id))
	return render_template("petrochemical_homepage.html", current_user = current_user, news = news)


########################################################################################
# Civil Department #

@dept_module.route('/Civil')
@login_required
def Civil():
	news = DepartmentNews.query.filter_by(dept = current_user.dept, news_for = 'department').order_by(desc(DepartmentNews.id))
	return render_template("civil_homepage.html", current_user = current_user, news = news)

@dept_module.route('/Civil/first_year')
@login_required
def Civil_first_year():
	news = DepartmentNews.query.filter_by(dept = current_user.dept, news_for = 'first_year').order_by(desc(DepartmentNews.id))
	return render_template("civil_homepage.html", current_user = current_user, news = news)

@dept_module.route('/Civil/second_year')
@login_required
def Civil_second_year():
	news = DepartmentNews.query.filter_by(dept = current_user.dept, news_for = 'second_year').order_by(desc(DepartmentNews.id))
	return render_template("civil_homepage.html", current_user = current_user, news = news)

@dept_module.route('/Civil/third_year')
@login_required
def Civil_third_year():
	news = DepartmentNews.query.filter_by(dept = current_user.dept, news_for = 'third_year').order_by(desc(DepartmentNews.id))
	return render_template("civil_homepage.html", current_user = current_user, news = news)

@dept_module.route('/Civil/final_year')
@login_required
def Civil_final_year():
	news = DepartmentNews.query.filter_by(dept = current_user.dept, news_for = 'final_year').order_by(desc(DepartmentNews.id))
	return render_template("civil_homepage.html", current_user = current_user, news = news)


########################################################################################
# Electronics Department #

@dept_module.route('/Electronics')
@login_required
def Electronics():
	news = DepartmentNews.query.filter_by(dept = current_user.dept, news_for = 'department').order_by(desc(DepartmentNews.id))
	return render_template("electronics_homepage.html", current_user = current_user, news = news)

@dept_module.route('/Electronics/first_year')
@login_required
def Electronics_first_year():
	news = DepartmentNews.query.filter_by(dept = current_user.dept, news_for = 'first_year').order_by(desc(DepartmentNews.id))
	return render_template("electronics_homepage.html", current_user = current_user, news = news)

@dept_module.route('/Electronics/second_year')
@login_required
def Electronics_second_year():
	news = DepartmentNews.query.filter_by(dept = current_user.dept, news_for = 'second_year').order_by(desc(DepartmentNews.id))
	return render_template("electronics_homepage.html", current_user = current_user, news = news)

@dept_module.route('/Electronics/third_year')
@login_required
def Electronics_third_year():
	news = DepartmentNews.query.filter_by(dept = current_user.dept, news_for = 'third_year').order_by(desc(DepartmentNews.id))
	return render_template("electronics_homepage.html", current_user = current_user, news = news)

@dept_module.route('/Electronics/final_year')
@login_required
def Electronics_final_year():
	news = DepartmentNews.query.filter_by(dept = current_user.dept, news_for = 'final_year').order_by(desc(DepartmentNews.id))
	return render_template("electronics_homepage.html", current_user = current_user, news = news)


########################################################################################
# Electrical Department # 

@dept_module.route('/Electrical')
@login_required
def Electrical():
	news = DepartmentNews.query.filter_by(dept = current_user.dept, news_for = 'department').order_by(desc(DepartmentNews.id))
	return render_template("electrical_homepage.html", current_user = current_user, news = news)

@dept_module.route('/Electrical/first_year')
@login_required
def Electrical_first_year():
	news = DepartmentNews.query.filter_by(dept = current_user.dept, news_for = 'first_year').order_by(desc(DepartmentNews.id))
	return render_template("electrical_homepage.html", current_user = current_user, news = news)

@dept_module.route('/Electrical/second_year')
@login_required
def Electrical_second_year():
	news = DepartmentNews.query.filter_by(dept = current_user.dept, news_for = 'second_year').order_by(desc(DepartmentNews.id))
	return render_template("electrical_homepage.html", current_user = current_user, news = news)

@dept_module.route('/Electrical/third_year')
@login_required
def Electrical_third_year():
	news = DepartmentNews.query.filter_by(dept = current_user.dept, news_for = 'third_year').order_by(desc(DepartmentNews.id))
	return render_template("electrical_homepage.html", current_user = current_user, news = news)

@dept_module.route('/Electrical/final_year')
@login_required
def Electrical_final_year():
	news = DepartmentNews.query.filter_by(dept = current_user.dept, news_for = 'final_year').order_by(desc(DepartmentNews.id))
	return render_template("electrical_homepage.html", current_user = current_user, news = news)


########################################################################################
# Mechanical Department #

@dept_module.route('/Mechanical')
@login_required
def Mechanical():
	news = DepartmentNews.query.filter_by(dept = current_user.dept, news_for = 'department').order_by(desc(DepartmentNews.id))
	return render_template("mechanical_homepage.html", current_user = current_user, news = news)

@dept_module.route('/Mechanical/first_year')
@login_required
def Mechanical_first_year():
	news = DepartmentNews.query.filter_by(dept = current_user.dept, news_for = 'first_year').order_by(desc(DepartmentNews.id))
	return render_template("mechanical_homepage.html", current_user = current_user, news = news)

@dept_module.route('/Mechanical/second_year')
@login_required
def Mechanical_second_year():
	news = DepartmentNews.query.filter_by(dept = current_user.dept, news_for = 'second_year').order_by(desc(DepartmentNews.id))
	return render_template("mechanical_homepage.html", current_user = current_user, news = news)

@dept_module.route('/Mechanical/third_year')
@login_required
def Mechanical_third_year():
	news = DepartmentNews.query.filter_by(dept = current_user.dept, news_for = 'third_year').order_by(desc(DepartmentNews.id))
	return render_template("mechanical_homepage.html", current_user = current_user, news = news)

@dept_module.route('/Mechanical/final_year')
@login_required
def Mechanical_final_year():
	news = DepartmentNews.query.filter_by(dept = current_user.dept, news_for = 'final_year').order_by(desc(DepartmentNews.id))
	return render_template("mechanical_homepage.html", current_user = current_user, news = news)



########################################################################################
# University news

@dept_module.route('/university_news')
def university_news():
	return render_template("university_news.html", current_user = current_user)
