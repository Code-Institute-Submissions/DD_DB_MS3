import os


class Config(object):
    MONGO_URI = os.environ.get('MONGO_URI')
    MONGO_DBNAME = "MUManager"
    SECRET_KEY = "powerful criptic key"
