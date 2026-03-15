from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# =========================
# USER TABLE
# =========================

class User(db.Model):

    __tablename__ = "user"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    email = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(100),
        nullable=False
    )

    role = db.Column(
        db.String(20),
        nullable=False
    )

    created_at = db.Column(
        db.DateTime
    )


# =========================
# STUDENT TABLE
# =========================

class Student(db.Model):

    __tablename__ = "student"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id")
    )

    first_name = db.Column(
        db.String(50)
    )

    last_name = db.Column(
        db.String(50)
    )

    college = db.Column(
        db.String(100)
    )

    skill = db.Column(
        db.String(100)
    )

    country = db.Column(
        db.String(50)
    )


# =========================
# CLIENT TABLE
# =========================

class Client(db.Model):

    __tablename__ = "client"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id")
    )

    first_name = db.Column(
        db.String(50)
    )

    last_name = db.Column(
        db.String(50)
    )

    country = db.Column(
        db.String(50)
    )