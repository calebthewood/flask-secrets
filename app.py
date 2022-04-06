import email
from flask import Flask, session, render_template, request, redirect, flash
from models import db, connect_db, User
from forms import RegisterForm, LoginForm, CSRFProtectForm
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///secrets"
app.config['SECRET_KEY'] = "secret"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()



@app.get("/")
def display_homepage():
    """Displays homepage"""

    return redirect("/register")


############################################################
#registration

@app.route("/register", methods=["GET", "POST"])
def register():
    """Handles user registration, adds username to session"""

    form = RegisterForm()

    if form.validate_on_submit():

        username = form.username.data
        password = form.password.data
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data

        user = User.register(username, password, email, first_name, last_name)
        db.session.add(user)
        db.session.commit()

        session["username"] = user.username
        return redirect(f"/users/{username}")

    return render_template("register.html", form=form)

############################################################
#login

@app.route("/login", methods=["GET", "POST"])
def login():
    """Produces login form and hanldes login"""

    form = LoginForm()

    if form.validate_on_submit():

        username = form.username.data
        password = form.password.data

        user = User.authentication(username, password)

        if user:
            session["username"] = user.username
            return redirect(f"/users/{username}")
        else:
            form.username.errors = ["Bad username/password"]

    return render_template("login.html", form=form)


@app.get("/users/<username>")
def shows_user_page(username):
    """Shows page for logged in user"""
     if session["username"] != username:
     flash("You must be logged in to view our awesome secret!!!")
     return redirect("/")

    user_notes = Notes.query.filter_by(owner=username)    

    user = User.query.get_or_404(username)
    return render_template("user.html", user=user)

############################################################
#logout

@app.post("/logout")
def logout():
    """Logs out and redirects to homepage"""

    form = CSRFProtectForm()    

    if form.validate_on_submit():
        session.pop("username",None)
    
    return redirect("/")

############################################################
#