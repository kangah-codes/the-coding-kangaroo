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
	__tablename__ = "user"

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	username = db.Column(db.String(), nullable=True)
	password = db.Column(db.String(), nullable=True)
	email = db.Column(db.String(), nullable=True)

	def __repr__(self):
		return f"User {self.id}, {self.username}"

class Post(db.Model):
	__tablename__ = 'posts'

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	title = db.Column(db.String(), nullable=True)
	banner_img_url = db.Column(db.String(), nullable=True)
	body = db.Column(db.String(), nullable=True)
	date = db.Column(db.DateTime, index=True, default=datetime.datetime.now())
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
