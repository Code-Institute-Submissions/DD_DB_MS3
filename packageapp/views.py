from packageapp import app, mongodb, bcrypt
from flask import render_template, redirect, request, url_for, flash, session
from datetime import datetime
from dateutil.relativedelta import relativedelta
from packageapp.forms import SigninForm, SignupForm, ProductForm
from bson.objectid import ObjectId


# Home Route
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="My Vanity")


# Products Route (Display)
@app.route("/products", methods=["GET", "POST"])
def products():
    if session.get("id") is None:
        flash("No Vanity is open")
        return redirect(url_for('signin'))
    # Original query & message
    message = ""
    query = {"user_id": session["id"]}
    '''
    POST product search filtering proccess function updating query
    merging dict condition for find() with the user imput
    '''
    if request.method == "POST":
        filterfunc = request.form.get("filter")
        if filterfunc:
            query_update = {"prodtype": filterfunc}
            query = {**query, **query_update}
    '''
    POST product search filtering proccess function updating query
    merging dict condition for find() with the user imput
    '''
    if request.method == "POST":
        brandfunc = request.form.get("brand").upper()
        if brandfunc:
            query_update = {"brand": {'$regex': brandfunc}}
            query = {**query, **query_update}

    # Updated query after POST brand.input and/or filter.input
    user_products = mongodb.db.products.find(query).sort("doe", -1)

    # Updated message after input fails to find()
    if mongodb.db.products.count_documents(query) == 0:
        filterfunc = request.form.get("filter")
        brandfunc = request.form.get("brand")
        if brandfunc and filterfunc:
            message = "No "+brandfunc.upper()+" "+filterfunc+" in your Vanity"
        elif brandfunc:
            message = "No " + brandfunc.upper() + " cosmetics in your Vanity"
        elif filterfunc:
            message = "No " + filterfunc + " cosmetics in your Vanity"
        else:
            message = "No cosmetics found in your Vanity"
    '''
    POST product search sorting proccess function using query
    update and using sort() with the user imput
    '''
    if request.method == "POST":
        sortfunc = request.form.get("sort")
        if sortfunc:
            user_products = user_products.sort(sortfunc, 1)

    prodtypes = mongodb.db.prodtypes
    products = mongodb.db.products
    return render_template("products.html", title="My Cosmetics",
                           prodtypes=prodtypes, products=products,
                           user_products=user_products, message=message)


# Delete Product Route (Delete)
@app.route("/deleteproduct/<product_id>", methods=["GET", "POST"])
def deleteproduct(product_id):
    if session.get("id") is None:
        flash("No Vanity is open")
        return redirect(url_for('signin'))

    products = mongodb.db.products
    product = products.find_one({"_id": ObjectId(product_id)})

    flash("{} from {} was successfully deleted".format(product["subtype"],
                                                       product["brand"]))
    products.remove({"_id": ObjectId(product_id)})

    return redirect(url_for('products'))


# Edit Product Route (Update)
@app.route("/editproduct/<product_id>", methods=["GET", "POST"])
def editproduct(product_id):
    if session.get("id") is None:
        flash("No Vanity is open")
        return redirect(url_for('signin'))

    prodtypes = mongodb.db.prodtypes
    product = mongodb.db.products.find_one({"_id": ObjectId(product_id)})

    # Secutiry measure checking item ownage
    if product["user_id"] != session.get("id"):
        flash("nice try tho")
        return redirect(url_for('index'))

    form = ProductForm()
    '''
    Populate wtform with data from our product at formulary load, placed on
    this route to avoid conflicts in process of data at submit to another
    '''
    form.brand.data = product["brand"]
    form.capacity.data = product["capacity"]
    form.dueperiod.data = product["due_time"]

    return render_template("editproduct.html", title="Edit Cosmetic",
                           prodtypes=prodtypes, product=product, form=form)


# Product Update Route (Update)
@app.route('/updateproduct/<product_id>', methods=["GET", "POST"])
def updateproduct(product_id):
    if session.get("id") is None:
        flash("No Vanity is open")
        return redirect(url_for('signin'))

    products = mongodb.db.products

    if request.form.get("dueperiod"):
        numbmonths = int(request.form["dueperiod"])
    if request.form.get("capacity"):
        capacity_data = int(request.form["capacity"])
    '''
    Date input conditionals and operations to get
    due date properly depending on switch choice
    '''
    if request.form.get("dou") != "":
        d_use = datetime.strptime(request.values.get("dou"), '%b %d, %Y')
        if type(request.form.get("duerelation")) is str:
            due_origin = request.values.get("dou")
        else:
            due_origin = request.values.get("dop")
    else:
        due_origin = request.values.get("dop")
        d_use = ""
    date_object = datetime.strptime(due_origin, '%b %d, %Y')
    due_date = date_object + relativedelta(months=numbmonths)
    due_string = due_date.strftime('%b %d, %Y')
    d_purchase = datetime.strptime(request.values.get("dop"), '%b %d, %Y')

    # Actual Updating
    products.update({"_id": ObjectId(product_id)},
                    {
                    "prodtype": request.form["prodtype"],
                    "subtype": request.form["subtype"],
                    "user_id": session.get("id"),
                    "brand": request.form["brand"].upper(),
                    "capacity": capacity_data,
                    "Date of Purchase": d_purchase,
                    "dop": request.form.get("dop"),
                    "Date of 1st Use": d_use,
                    "dou": request.form.get("dou"),
                    "due_time": numbmonths,
                    "due_in": request.values.get("duerelation"),
                    "Due Date": due_date,
                    "dd": due_string,
                    "doe": datetime.utcnow(),
                    })
    item = mongodb.db.products.find_one({"_id": ObjectId(product_id)})
    flash("{} from {} was Successfully Updated".format(item["subtype"],
                                                       item["brand"]))

    return redirect(url_for('products'))


# Add Product Route (Create)
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
        due date properly depending on switch choice
        '''
        if request.form["dou"] != "":
            d_use = datetime.strptime(request.values.get("dou"), '%b %d, %Y')
            if type(request.form.get("duerelation")) is str:
                due_origin = request.values.get("dou")
            else:
                due_origin = request.values.get("dop")
        else:
            due_origin = request.values.get("dop")
            d_use = ""
        date_object = datetime.strptime(due_origin, '%b %d, %Y')
        due_date = date_object + relativedelta(months=numbmonths)
        due_string = due_date.strftime('%b %d, %Y')
        d_purchase = datetime.strptime(request.values.get("dop"), '%b %d, %Y')

        # New document creation
        new_product = {
            "prodtype": request.form["prodtype"],
            "subtype": request.form["subtype"],
            "user_id": session.get("id"),
            "brand": request.form["brand"].upper(),
            "capacity": capacity_data,
            "Date of Purchase": d_purchase,
            "dop": request.form["dop"],
            "Date of 1st Use": d_use,
            "dou": request.form["dou"],
            "due_time": numbmonths,
            "due_in": request.values.get("duerelation"),
            "Due Date": due_date,
            "dd": due_string,
            "doe": datetime.utcnow()
            }
        products.insert_one(new_product)
        flash("Product added to your Vanity")
        return redirect(url_for('index'))

    prodtypes = mongodb.db.prodtypes

    return render_template("addproduct.html", title="Add Cosmetic", form=form,
                           prodtypes=prodtypes)


# Sign Up Route (Create)
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


# Sign In Route (Display)
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


# Error Handling Route
@app.errorhandler(Exception)
def errorhandler(e):
    flash("Cosmetics were taking the wrong path... But all is good back at your Vanity")
    return redirect(url_for('index'))
