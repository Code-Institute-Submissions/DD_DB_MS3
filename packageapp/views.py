from packageapp import app, mongodb
from flask import render_template, redirect, request, url_for, flash
from packageapp.forms import SigninForm, SignupForm

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="Index", makeups=mongodb.db.makeups.find())

@app.route("/products", methods=["GET", "POST"])
def products():
    return render_template("products.html", title="My products")

@app.route("/editproduct", methods=["GET", "POST"])
def editproduct():
    return render_template("editproduct.html", title="Edit Product")

@app.route("/addproduct", methods=["GET", "POST"])
def addproduct():
    return render_template("addproduct.html", title="Add Product")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    return render_template("signup.html", title="")

@app.route("/signin", methods=["GET", "POST"])
def signin():
    form = SigninForm()
    if form.validate_on_submit():
        flash("Login successfull, {}".format(form.user_name.data))
        return redirect("/index")
    return render_template("signin.html", title="Sign In", form=form)
