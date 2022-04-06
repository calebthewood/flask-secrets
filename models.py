"""Models"""
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

def connect_db(app):
    """Connect DB to Flask"""
    db.app = app
    db.init_app(app)

class User(db.Model):
    """User Model"""

    __tablename__ = "users"

    username = db.Column(
        db.Text(),
        primary_key=True)

    password = db.Column(
        db.Text(),
        nullable=False)

    email = db.Column(
        db.Text(),
        nullable=False)

    first_name = db.Column(
        db.Text(),
        nullable=False)

    last_name = db.Column(
        db.Text(),
        nullable=False
    )

    @classmethod
    def register(cls, username, password, email, first_name, last_name):
        """Registers user with hashed password and returns User instance
        """
        hashed = bcrypt.generate_password_hash(password).decode('utf8')

        return cls(username=username,
                 password=hashed,
                 email=email,
                 first_name=first_name,
                 last_name=last_name)


    @classmethod
    def authentication(cls, username, password):

        u = cls.query.filter_by(username=username).one_or_none()

        if u and bcrypt.check_password_hash(u.password, password):
            return u
        else:
            False


class Note(db.Model):
    """Note Model"""

    __tablename__ = "notes"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True)

    title = db.Column(
        db.String(100),
        nullable=False)

    content = db.Column(
        db.Text,
        nullable=False)

    owner = db.Column(
        db.Text(),
        nullable=False,
        ForeignKey('users.username'))
    )