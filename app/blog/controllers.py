# your app controllers
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from app.blog.models import *
from app.blog.parser import *

controller = Blueprint('blog', __name__)

@controller.route('/')
def index():
	return render_template('index.html')

@controller.route('/post')
def post():
	return render_template('post.html')