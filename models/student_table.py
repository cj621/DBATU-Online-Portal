from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin

from db_init import db

class Students(UserMixin, db.Model):
	__tablename__ = 'students'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255))
	dept = db.Column(db.String(255))
	year = db.Column(db.Integer)
	email = db.Column(db.String(255))
	password = db.Column(db.String(255))