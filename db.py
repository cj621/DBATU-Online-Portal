from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:chitts@localhost/bhendi'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret key'

db = SQLAlchemy(app)

class Students(UserMixin, db.Model):
	__tablename__ = 'students'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255))
	dept = db.Column(db.String(255))
	year = db.Column(db.Integer)
	email = db.Column(db.String(255))
	password = db.Column(db.String(255))