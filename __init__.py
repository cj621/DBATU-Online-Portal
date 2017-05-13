from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:chitts@localhost/bhendi'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret key'


#Blueprints
from department import dept_module
app.register_blueprint(dept_module)

from university import university_module
app.register_blueprint(university_module)

#DB object
from db_init import db
db.init_app(app)