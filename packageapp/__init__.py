from flask import Flask
from config import Config
import os
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config.from_object(Config)
db = PyMongo(app)

from packageapp import views
