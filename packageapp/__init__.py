import os
from flask import Flask, url_for
from config import Config
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config.from_object(Config)
mongodb = PyMongo(app)
bcrypt = Bcrypt(app)

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
