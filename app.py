import email
from flask import Flask, session, render_template, request, redirect
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


@app.route("/register", methods=["GET", "POST"])
def register():


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
        return redirect("/secret")

    return render_template("register.html", form=form)



@app.route("/login", methods=["GET", "POST"])
def login():


  return render_template("login.html")


@app.get("/secret")
def secret():
    breakpoint()

    return ("secrets.html")