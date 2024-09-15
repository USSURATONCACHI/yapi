from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask('YAPI')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///default.db'
db = SQLAlchemy(app)

config = {}