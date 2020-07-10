from packageapp import app, mongodb
from flask import render_template, redirect, request, url_for, flash
from packageapp.forms import SigninForm, SignupForm


@app.route("/")
@app.route("/index")
def index():
    makeups = mongodb.db.makeups.find()
    return render_template("index.html", title="Index", makeups=makeups)


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
    form = SignupForm()
    if form.validate_on_submit():
        users = mongodb.db.users
        old_user = users.find_one({"name": request.form["username"].lower()})
        
        if old_user is None:
            password_hash = ""
            new_user = {"name": request.form["username"].lower(), "password": password_hash}
            users.insert_one(new_user)
            flash("{}'s vanity created".format(form.username.data))
            return redirect("/signin")
        else:
            flash("That vanity name is taken")
            return redirect("/signup")
            
    return render_template("signup.html", title="Sign Up", form=form)


@app.route("/signin", methods=["GET", "POST"])
def signin():
    form = SigninForm()
    if form.validate_on_submit():
        flash("Your vanity is ready, {}".format(form.username.data))
        return redirect("/index")
    return render_template("signin.html", title="Sign In", form=form)
