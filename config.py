import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'it_is_my_secret_key'
