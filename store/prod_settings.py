import os

from .settings import *

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = ['peaceful-escarpment-54364.herokuapp.com']
