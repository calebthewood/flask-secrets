from flask import Flask, jsonify, render_template, request
from models import db, connect_db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///secrets"
app.config['SECRET_KEY'] = "secret"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

@app.get("/")
def display_homepage():
    """Displays homepage"""

    return render_template('#add homepage')
