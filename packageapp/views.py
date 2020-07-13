from packageapp import app, mongodb, bcrypt
from flask import render_template, redirect, request, url_for, flash, session
from datetime import datetime
from packageapp.forms import SigninForm, SignupForm, ProductForm


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="Index")


@app.route("/products", methods=["GET", "POST"])
def products():
    if session.get("id") is None:
        flash("No Vanity is open")
        return redirect(url_for('signin'))

    return render_template("products.html", title="My products")


@app.route("/editproduct", methods=["GET", "POST"])
def editproduct():
    if session.get("id") is None:
        flash("No Vanity is open")
        return redirect(url_for('signin'))
    return render_template("editproduct.html", title="Edit Product")


@app.route("/addproduct", methods=["GET", "POST"])
def addproduct():
    if session.get("id") is None:
        flash("No Vanity is open")
        return redirect(url_for('signin'))

    form = ProductForm()
    prodtypes = mongodb.db.prodtypes.find()
    prodtypes2 = mongodb.db.prodtypes.find()

    return render_template("addproduct.html", title="Add Product", form=form,
                           prodtypes=prodtypes, prodtypes2=prodtypes2,
                           products=products)


@app.route("/insertproduct", methods=["GET", "POST"])
def insertproduct():
    products = mongodb.db.products

    new_product = {
        "user_id": session.get("id"),
        "brand": request.form["brand"],
        "capacity": request.form["capacity"],
        "doe": datetime.utcnow()
        }
    products.insert_one(new_product)
    flash("Product added to your Vanity")
    return redirect(url_for('addproduct'))


@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()

    if form.validate_on_submit():
        users = mongodb.db.users
        old_user = users.find_one({"name": request.form["username"].lower()})

        if old_user is None:
            password_hash = bcrypt.generate_password_hash(
                request.form["password"]).decode("utf-8")
            new_user = {
                "name": request.form["username"].lower(),
                "email": request.form["email"],
                "password": password_hash,
                "dateosu": datetime.utcnow()
                }
            users.insert_one(new_user)
            flash("{}'s Vanity created".format(form.username.data))
            return redirect(url_for('signin'))

        flash("That Vanity Name is taken")
        return redirect(url_for('signup'))

    return render_template("signup.html", title="Sign Up", form=form)


@app.route("/signin", methods=["GET", "POST"])
def signin():
    form = SigninForm()
    users = mongodb.db.users

    if form.validate_on_submit():
        password = request.form["password"]
        user = request.form["username"]
        user_signing = users.find_one({"name": user.lower()})

        if user_signing is None:
            flash("Vanity Name doesn't exist")
            return redirect(url_for('signin'))

        if bcrypt.check_password_hash(user_signing["password"], password):
            user_id = str(user_signing["_id"])
            session["id"] = user_id
            session["name"] = user
            flash("Your Vanity is ready, {}".format(form.username.data))
            return redirect(url_for('index'))

        flash("Vanity Name and Password don't match")
        return redirect(url_for('signin'))

    return render_template("signin.html", title="Sign In", form=form)


@app.route('/signout')
def signout():
    if session.get("id") is None:
        return redirect(url_for('signin'))
    session.pop("id", None)
    flash("Vanity closed successfully")
    return redirect(url_for('index'))
