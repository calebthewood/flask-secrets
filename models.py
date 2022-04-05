"""Models"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect DB to Flask"""
    db.app = app
    db.init_app(app)

#add User Model etc.
# username - textual primary key that is no longer than 20 characters.
# password - not-nullable column that is a string no longer than 100 characters (will store hashed passwords).
# email - not-nullable column that is unique and no longer than 50 characters.
# first_name - not-nullable column that is no longer than 30 characters.
# last_name - not-nullable column that is no longer than 30 characters.

class User(db.Model):
    """User Model"""

    __tablename__ = "secrets"

    username = db.Column(
        db.Text(20),
        primary_key=True)

    password = db.Column(
        db.Text(100),
        nullable=False)

    #check iof SQLA validates for email?
    email = db.Column(
        db.Text(),
        nullable=False)

    first_name = db.Column(
        db.Text(30),
        nullable=False)

    last_name = db.Column(
        db.Text(30),
        nullable=False
    )

    @classmethod
    #authentication function