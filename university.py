from flask import Blueprint
from flask import Flask, request, url_for, render_template, redirect, flash, send_from_directory
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import datetime
from sqlalchemy import desc
from werkzeug import secure_filename
import os

university_module = Blueprint('university', __name__)

from models.universitynews_table import *

from __init__ import app

# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = 'uploads/'
# folder
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@university_module.route('/university_post', methods = ['POST'])
@login_required
def university_post():

	# Get the name of the uploaded file
	file_content = request.files['inputfile']
	# Check if the file is one of the allowed types/extensions
	if file_content and allowed_file(file_content.filename):
		# Make the filename safe, remove unsupported chars
		filename = secure_filename(file_content.filename)
        # Move the file form the temporal folder to
        # the upload folder we setup
        file_content.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))



	id = datetime.now()
	dept = request.form['news_category']
	news = request.form['newsdetail']
	file_name = filename
	posted_by = current_user.name

	new_university_post = UniversityNews(id=id, dept=dept, news=news, file_name = file_name, posted_by=posted_by)
	db.session.add(new_university_post)
	db.session.commit()

	return redirect(url_for('university.university_news', section=dept))
	


@university_module.route('/university_news/<section>')
@login_required
def university_news(section):
	news = UniversityNews.query.filter_by(dept = section).order_by(desc(UniversityNews.id))
	return render_template("university_news.html", current_user = current_user, news = news)



# This route is expecting a parameter containing the name
# of a file. Then it will locate that file on the upload
# directory and show it on the browser, so if the user uploads
# an image, that image is going to be show after the upload
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment = True)
