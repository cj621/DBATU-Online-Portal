from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from datetime import datetime

from db_init import db

class DepartmentNews(UserMixin, db.Model):
	__tablename__ = 'departmentnews'
	id = db.Column(db.DateTime(timezone=False), primary_key=True)
	dept = db.Column(db.String(255))
	news_for = db.Column(db.String(255))
	news = db.Column(db.String(1023))
	posted_by = db.Column(db.String(255))