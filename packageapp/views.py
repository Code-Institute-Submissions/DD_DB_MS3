from packageapp import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="Index")

@app.route("/products")
def products():
    return render_template("products.html", title="My products")

@app.route("/editproduct")
def editproduct():
    return render_template("editproduct.html", title="Edit Product")

@app.route("/addproduct")
def addproduct():
    return render_template("addproduct.html", title="Add Product")

@app.route("/signup")
def signup():
    return render_template("signup.html", title="")

@app.route("/signin")
def signin():
    return render_template("signin.html", title="")
