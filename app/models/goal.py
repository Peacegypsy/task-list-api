from flask import current_app
from app import db
from sqlalchemy import ForeignKey, update
from sqlalchemy.orm import relationship


class Goal(db.Model):
    goal_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    tasks = db.relationship('Task', backref='tasks', lazy=True)
