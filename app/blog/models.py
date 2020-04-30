# your models go here
from app import db, flask_bcrypt, login
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
import json
import uuid
import string
import random
import datetime

class User(db.Model):
	__tablename__ = "admin"

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	username = db.Column(db.String(), nullable=True)
	password = db.Column(db.String(), nullable=True)

	def __repr__(self):
		return f"User {self.id}, {self.username}"

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
