from flask import Flask
from app import db
from flask.ext.security import UserMixin, RoleMixin
	
# Define models
roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    address = db.Column(db.String(255))
    number = db.Column(db.String(255))
    address2 = db.Column(db.String(255))
    neighbourhood = db.Column(db.String(255))
    zipcode = db.Column(db.String(255))
    city = db.Column(db.String(255))
    state = db.Column(db.String(255))
    birthday = db.Column(db.String(255))
    cellphone = db.Column(db.String(255))
    phone = db.Column(db.String(255))


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lastName = db.Column(db.String(255), index=True)
    firstName = db.Column(db.String(255), index=True)
    address = db.Column(db.String(255), index=True)
    city = db.Column(db.String(255), index=True)

    def __repr__(self):
        return '<Person %r>' % (self.lastName)