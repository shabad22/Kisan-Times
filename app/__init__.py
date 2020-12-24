from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = '21dc6ebfa6175fda2e66a757eb1c10c8'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

database = SQLAlchemy(app)

# Dont move this import above the database instance or it will cuase circular import errors
from app import routes