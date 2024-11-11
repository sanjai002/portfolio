# app.py
import os
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_uploads import UploadSet, configure_uploads, IMAGES
from models import db, Skill, Project

# Initialize the Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "supersecretkey"

# Configure file upload for images
app.config['UPLOADED_IMAGES_DEST'] = os.path.join(os.path.dirname(__file__), 'static', 'images')
images = UploadSet('images', IMAGES)
configure_uploads(app, images)

# Initialize database and Flask-Admin
db.init_app(app)
admin = Admin(app, name='Admin Panel', template_mode='bootstrap3')

# Define Admin ModelViews with image upload support
from flask_admin.form import FileUploadField

class SkillAdmin(ModelView):
    form_overrides = {
        'image_filename': FileUploadField
    }
    form_args = {
        'image_filename': {
            'label': 'Image',
            'base_path': app.config['UPLOADED_IMAGES_DEST'],
            'allow_overwrite': True
        }
    }

class ProjectAdmin(ModelView):
    form_overrides = {
        'image_filename': FileUploadField
    }
    form_args = {
        'image_filename': {
            'label': 'Image',
            'base_path': app.config['UPLOADED_IMAGES_DEST'],
            'allow_overwrite': True
        }
    }

# Add models to the admin interface
admin.add_view(SkillAdmin(Skill, db.session))
admin.add_view(ProjectAdmin(Project, db.session))

# Create tables on first request
@app.before_first_request
def create_tables():
    db.create_all()

# Main route
@app.route("/")
def index():
    skills = Skill.query.all()
    projects = Project.query.all()
    return render_template("index.html", skills=skills, projects=projects)

# Run the application
if __name__ == "__main__":
    app.run(debug=True)
