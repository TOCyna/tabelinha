import os.path
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import Security, SQLAlchemyUserDatastore

app = Flask(__name__)
app.config.from_object('config')

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'super-secret'
app.config['SECURITY_REGISTERABLE'] = True

db = SQLAlchemy(app)


from app import views, models, forms
from .models import User, Role

user_datastore = SQLAlchemyUserDatastore(db, User, Role)

from forms import ExtendedRegisterForm

security = Security(app, user_datastore,
         register_form=ExtendedRegisterForm)

# Mail function used by security
from flask_mail import Mail

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'tocynamata@gmail.com'
app.config['MAIL_PASSWORD'] = 'Tocyna28'
mail = Mail(app)