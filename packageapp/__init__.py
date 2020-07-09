from flask import Flask, url_for
from config import Config
import os
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config.from_object(Config)
mongodb = PyMongo(app)

from packageapp import views

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
