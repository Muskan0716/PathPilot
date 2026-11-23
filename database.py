
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()


# USER TABLE
class User(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    email = db.Column(
        db.String(150),
        unique=True,
        nullable=False
    )

    password_hash = db.Column(
        db.String(255),
        nullable=False
    )

    education = db.Column(db.String(150), default="")

    courses = db.Column(db.Text, default="")

    interests = db.Column(db.Text, default="")

    career_interests = db.Column(db.Text, default="")

    skills = db.Column(db.Text, default="")

    is_admin = db.Column(
        db.Boolean,
        default=False,
        nullable=False
    )


# PROGRESS TABLE
class Progress(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=False
    )

    task = db.Column(db.String(250), nullable=False)

    completed = db.Column(db.Boolean, default=False)


# SKILL ASSESSMENT TABLE
class SkillAssessment(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=False
    )

    career_slug = db.Column(
        db.String(100),
        nullable=False
    )

    career_name = db.Column(
        db.String(150),
        nullable=False
    )

    matched_skills = db.Column(db.Text, default="")

    missing_skills = db.Column(db.Text, default="")

    match_percentage = db.Column(
        db.Integer,
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


# CAREER APTITUDE RESULT TABLE
class AptitudeResult(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=False
    )

    answers = db.Column(db.Text, nullable=False)

    scores = db.Column(db.Text, nullable=False)

    recommended_career = db.Column(
        db.String(150),
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


# RESUME ANALYSIS TABLE
class ResumeAnalysis(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=False
    )

    filename = db.Column(
        db.String(255),
        nullable=False
    )

    detected_skills = db.Column(
        db.Text,
        default=""
    )

    missing_skills = db.Column(
        db.Text,
        default=""
    )

    match_percentage = db.Column(
        db.Integer,
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )
