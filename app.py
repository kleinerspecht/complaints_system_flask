from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
db = SQLAlchemy(app)

class BaseUser(db.Model):
    pass
