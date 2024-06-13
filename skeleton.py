import os
import subprocess

def create_skeleton():
    # Get User Inputs
    project_name = input("Enter the project name (snake_case): ")
    blueprints = input("Enter blueprint names (snake_case, comma separated): ").split(',')
    dependencies = input("Enter dependencies (comma separated) or leave blank for default").split(',')

    if dependencies == ['']:
        # TODO TODO-FIRST set your default dependencies, or use mine
        dependencies = ['Flask', 'Flask-CKEditor', 'Flask-Mail', 'Flask-Login', 'Flask-Migrate', 
                        'Flask-SQLAlchemy', 'Flask-WTF', 'email_validator', 'python-dotenv']
    
    #TODO TODO-FIRST Update base_dir variable.
    # Note: can set base_dir = an absolute path, if desired (this is probably best practice)
    # if you're using a local path instead of an absolute one:
    # make sure you're running skeleton.py FROM THE DIRECTORY you want to create the base_dir in
    # ex: move it to a repos folder and run it from there, creating a subdirectory in repos with whatever name you set to base_dir
    # or just use an absolute path (to the folder you want your project in)


    # set base directory and create folder if not exists
    base_dir = 'flask_projects'
    os.makedirs(base_dir, exist_ok=True)
    
    
    # Set base project_path variable and create that directory
    project_path = os.path.join(base_dir, project_name)
    os.makedirs(project_path)

    #create a virtual environment
    subprocess.run(['python', '-m', 'venv', os.path.join(project_path, 'venv')])

    # main project structure
    os.makedirs(os.path.join(project_path, f'{project_name}'))
    os.makedirs(os.path.join(project_path, f'{project_name}', 'templates'))
    os.makedirs(os.path.join(project_path, f'{project_name}', 'static'))

    # create base.html with bootstrap added
    with open(os.path.join(project_path, f'{project_name}/templates/base.html'), 'w') as f:
        f.write(f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>
    <!--TODO add title in double brackets, update default title if needed-->
    {{title}}</title>
    
    <!-- add bootstrap -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    
    <!-- add static styles -->
    <!--TODO add url_for in double brackets -->
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
                
    {{% block head%}} {{% endblock head %}} </head>
  <body>
        {{% block content %}}
        {{% endblock content %}}
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
  </body>
</html>""")
        

    # create styles.css
    with open(os.path.join(project_path, f'{project_name}/static/styles.css'), 'w') as f:
        f.write("/* Styles will go here */")

    # create blueprints
    for bp in blueprints:
        bp = bp.strip()
        if bp:
            bp_dir = os.path.join(project_path, f'{project_name}', bp)
            # Create blueprint folders
            os.makedirs(bp_dir)
            os.makedirs(os.path.join(bp_dir, 'templates'))
            os.makedirs(os.path.join(bp_dir, 'static'))

            # Create blueprint routes.py
            with open (os.path.join(bp_dir, 'routes.py'), 'w') as f:
                f.write(f"""from flask import Blueprint, redirect, url_for, flash, request, render_template
{bp} = Blueprint('{bp}', __name__, template_folder='templates', static_folder='static', static_url_path='/{bp}/static')

@{bp}.route('/{bp}_home')
def {bp}_home():
    return 'Hello, {bp.capitalize()}!'
 """)
            # Create blueprint __init__.py    
            with open (os.path.join(bp_dir, '__init__.py'), 'w') as f:
                f.write(f"from .routes import {bp}")

            # Create blueprint forms.py
            with open (os.path.join(bp_dir, 'forms.py'), 'w') as f:
                f.write("""from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, PasswordField, BooleanField, SubmitField, DateField, TimeField
from wtforms.validators import DataRequired, ValidationError, EqualTo, Email, InputRequired, Optional""")

    # create bp_import and registration strings to add to __init__.py
    blueprint_imports = "\n        ".join([f"from {project_name}.{bp.strip()} import {bp.strip()} as {bp.strip()}_bp" for bp in blueprints if bp.strip()])
    blueprint_registrations = "\n        ".join([f"app.register_blueprint({bp.strip()}_bp)" for bp in blueprints if bp.strip()])

    # Create __init__.py
    with open(os.path.join(project_path, f'{project_name}', '__init__.py'), 'w') as f:
        f.write(f"""import os
# TODO remove unnecessary imports
                
from flask import Flask
from sqlalchemy import MetaData

from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_ckeditor import CKEditor
from flask_login import LoginManager

metadata = MetaData(
    naming_convention={{
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
    }}
)

#TODO update the below lines if needed, to remove unused libraries

db = SQLAlchemy(metadata=metadata)
migrate = Migrate()
mail = Mail()
ckeditor = CKEditor()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static/uploads') # TODO change name of uploads folder if needed
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    #TODO update the below lines to remove unused libraries
    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)
    mail.init_app(app)
    ckeditor.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        from {project_name} import routes, models
        {blueprint_imports}

        {blueprint_registrations}

    return app
""")

    # Create main routes.py
    with open(os.path.join(project_path, f'{project_name}', 'routes.py'), 'w') as f:
        f.write("""from flask import current_app as app, render_template, request, url_for, flash

@app.route('/')
def home():
    return render_template('base.html') #TODO Update primary route
""")       

    # Create models_base, with User model
    models_base = f"""from {project_name} import db, login_manager
from sqlalchemy.ext.associationproxy import association_proxy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import URLSafeTimedSerializer as Serializer, SignatureExpired
import os

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(50))
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(os.environ.get('SECRET_KEY'), expires_sec)
        return s.dumps(self.email, salt='password-reset')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(os.environ.get('SECRET_KEY'))
        try:
            email = s.loads(token, salt='password-reset')
        except:
            return None
        return User.query.filter_by(email=email).first()
#TODO Update Models, then run flask db init, then flask db migrate
"""
    # if auth isn't in blueprints, update models_base to not include the User model
    if 'auth' not in blueprints:
        models_base = f"""from {project_name} import db
from sqlalchemy.ext.associationproxy import association_proxy

#TODO Update Models, then run flask db init, then flask db migrate
"""
    
    # Create models.py
    with open(os.path.join(project_path, f'{project_name}', 'models.py'), 'w') as f:
        f.write(f"{models_base}")


    # Create main.py
    with open(os.path.join(project_path, 'main.py'), 'w') as f:
        f.write(f"""from {project_name} import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
                
# TODO activate venv by running venv/Scripts/activate <--- use backslash, not /
# TODO (once venv is activated) install requirements by running pip install -r requirements.txt 
""")

    # Create config.py
    with open(os.path.join(project_path, 'config.py'), 'w') as f:      
        # TODO TODO-FIRST update your config set up (remove the mail stuff if you dont need it, etc)
        f.write(f"""import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'this-is-secret'
    # TODO update db name if needed
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///{project_name}.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # TODO Update your mail settings if needed
    MAIL_SERVER = 'smtp-mail.outlook.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
""")
    
    # Create .flaskenv
    with open(os.path.join(project_path, '.flaskenv'), 'w') as f:
        f.write("FLASK_APP=main.py")

    # Create .env
    with open(os.path.join(project_path, '.env'), 'w') as f:
        #TODO TODO-FIRST update your environment variables
        f.write("""
SECRET_KEY='THISISASECRET'
MAIL_USERNAME='yournamehere@test.com'
MAIL_PASSWORD='totallyrealpassword'
""")
    
    # Create requirements.txt
    with open(os.path.join(project_path, 'requirements.txt'), 'w') as f:
        for dependency in dependencies:
            dependency = dependency.strip()
            if dependency:
                f.write(f'{dependency}\n')

    print(f"Flask project {project_name} created in {project_path}! \n Check TODOs to ensure any config is taken care of")

if __name__ == "__main__":
    create_skeleton()
