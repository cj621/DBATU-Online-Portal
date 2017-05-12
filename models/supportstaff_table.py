from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin

from db_init import db

class SupportStaff(UserMixin, db.Model):
	__tablename__ = 'supportstaff'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(255))
	password = db.Column(db.String(255))
	name = db.Column(db.String(255))
	dept = db.Column(db.String(255))
	email = db.Column(db.String(255))