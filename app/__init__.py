from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import Security, SQLAlchemyUserDatastore

app = Flask(__name__)
app.config.from_object('config')

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'super-secret'

db = SQLAlchemy(app)


from app import views, models
from .models import User, Role

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

@app.before_first_request
def create_user():
    db.create_all()
    user_datastore.create_user(email='eugriner@gmail.com', password='280689')
    db.session.commit()