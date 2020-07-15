from packageapp import app, mongodb, bcrypt
from flask import render_template, redirect, request, url_for, flash, session
from datetime import datetime
from dateutil.relativedelta import relativedelta
from packageapp.forms import SigninForm, SignupForm, ProductForm


# Home Route
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="Index")


# Products Route
@app.route("/products", methods=["GET", "POST"])
def products():
    if session.get("id") is None:
        flash("No Vanity is open")
        return redirect(url_for('signin'))

    prodtypes = mongodb.db.prodtypes
    products = mongodb.db.products.find({"user_id": session["id"]})

    if request.method == "POST":
        products = products.filter({""})

    return render_template("products.html", title="My products",
                           prodtypes=prodtypes, products=products)


# Edit Product Route
@app.route("/editproduct", methods=["GET", "POST"])
def editproduct():
    if session.get("id") is None:
        flash("No Vanity is open")
        return redirect(url_for('signin'))
    return render_template("editproduct.html", title="Edit Product")


# Add Product Route
@app.route("/addproduct", methods=["GET", "POST"])
def addproduct():
    if session.get("id") is None:
        flash("No Vanity is open")
        return redirect(url_for('signin'))

    form = ProductForm()

    if form.validate_on_submit():
        products = mongodb.db.products
        numbmonths = int(request.form["dueperiod"])
        capacity_data = int(request.form["capacity"])
        '''
        Date input conditionals and operations to get
        due date properly depending on choice
        '''
        if request.form["dou"] != "":
            if type(request.form.get("duerelation")) is str:
                due_origin = request.values.get("dou")
            else:
                due_origin = request.values.get("dop")
        else:
            due_origin = request.values.get("dop")
        date_object = datetime.strptime(due_origin, '%b %d, %Y')
        due_date = date_object + relativedelta(months=numbmonths)
        due_string = due_date.strftime('%b %d, %Y')

        # New document creation
        new_product = {
            "prodtype": request.form["prodtype"],
            "subtype": request.form["subtype"],
            "user_id": session.get("id"),
            "brand": request.form["brand"],
            "capacity": capacity_data,
            "Date of Purchase": request.form["dop"],
            "Date of 1st Use": request.form["dou"],
            "due_time": numbmonths,
            "due_in": request.values.get("duerelation"),
            "Due Date": due_string,
            "doe": datetime.utcnow()
            }
        products.insert_one(new_product)
        flash("Product added to your Vanity")
        return redirect(url_for('index'))

    prodtypes = mongodb.db.prodtypes

    return render_template("addproduct.html", title="Add Product", form=form,
                           prodtypes=prodtypes)


# Sign Up Route
@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()

    if form.validate_on_submit():
        users = mongodb.db.users
        old_user = users.find_one({"name": request.form["username"].lower()})

        if old_user is None:
            password_hash = bcrypt.generate_password_hash(
                request.form["password"]).decode("utf-8")
            # New user creation
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


# Sign In Route
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


# Sign Out Route
@app.route('/signout')
def signout():
    if session.get("id") is None:
        return redirect(url_for('signin'))
    session.pop("id", None)
    flash("Vanity closed successfully")
    return redirect(url_for('index'))
