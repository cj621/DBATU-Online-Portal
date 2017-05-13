from flask import Blueprint
from flask import Flask, request, url_for, render_template, redirect, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import datetime
from sqlalchemy import desc

university_module = Blueprint('university', __name__)

from models.universitynews_table import *


@university_module.route('/university_post', methods = ['POST'])
@login_required
def university_post():
	id = datetime.now()
	dept = request.form['news_category']
	news = request.form['newsdetail']
	posted_by = current_user.name

	new_university_post = UniversityNews(id=id, dept=dept, news=news, posted_by=posted_by)
	db.session.add(new_university_post)
	db.session.commit()

	return redirect(url_for('university.university_news', section=dept))
	


@university_module.route('/university_news/<section>')
def university_news(section):
	news = UniversityNews.query.filter_by(dept = section).order_by(desc(UniversityNews.id))
	return render_template("university_news.html", current_user = current_user, news = news)

