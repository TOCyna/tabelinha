from flask import Flask, render_template, flash, redirect
from app import app, db
from .forms import InsertForm
from .models import Person, User, Role
from flask.ext.security import login_required, logout_user, current_user


@app.route('/', methods=['GET', 'POST'])
@login_required
def index():

    form = InsertForm()
    if form.validate_on_submit():
        lastName = form.lastName.data
        firstName = form.firstName.data
        address = form.address.data
        city = form.city.data
        person = Person(lastName = lastName, firstName = firstName, 
            address = address, city = city)
        db.session.add(person)
        db.session.commit()

    persons = Person.query.all()
    users = User.query.all()
    u = current_user
    return render_template("index.html",
                           title='Agenda',
                           persons=persons,
                           form=form, users=users, u=u )

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')
