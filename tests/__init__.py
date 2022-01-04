from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv, path
import uuid

 
app = Flask(__name__)
 
app.config['SQLALCHEMY_DATABASE_URI'] = getenv("DATABASE_URI")
 
app.config['SECRET_KEY'] = str(uuid.uuid4())
 
db = SQLAlchemy(app)

DB_Name = "database.db"
 
 

def create_database(app):
    if not path.exists('application/' + DB_Name):
        db.create_all(app=app)
        print('Created Database!')

create_database(app)

 
 
 
from application import routes




