# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    image_filename = db.Column(db.String(100), nullable=True)  # Field for storing image filename

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_filename = db.Column(db.String(100), nullable=True)  # Field for storing image filename
    link = db.Column(db.String(200), nullable=True)
