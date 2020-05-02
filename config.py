# your configs go here

# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os
import sqlalchemy
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')
	DEBUG = False

class DevelopmentConfig(Config):
	BASE_DIR = os.path.abspath(os.path.dirname(__file__))  
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'development.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	DATABASE_CONNECT_OPTIONS = {}
	THREADS_PER_PAGE = 2
	CSRF_ENABLED = True
	CSRF_SESSION_KEY = "secret"
	SECRET_KEY = "secret"
	DEBUG = True

class TestingConfig(Config):
	DEBUG = True
	TESTING = True
	BASE_DIR = os.path.abspath(os.path.dirname(__file__))  
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'test.db')
	PRESERVE_CONTEXT_ON_EXCEPTION = False
	SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
	DEBUG = False
	TESTING = False
	BASE_DIR = os.path.abspath(os.path.dirname(__file__))  
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'production.db')
	PRESERVE_CONTEXT_ON_EXCEPTION = False
	SQLALCHEMY_TRACK_MODIFICATIONS = True
	DATABASE_CONNECT_OPTIONS = {}
	THREADS_PER_PAGE = 2
	CSRF_ENABLED     = True
	CSRF_SESSION_KEY = "secret"
	SECRET_KEY = "secret"

config_by_name = dict(
    dev=DevelopmentConfig,
)