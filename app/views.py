from flask import render_template, flash, redirect
from app import app, db
from .forms import InsertForm
from .models import Person


@app.route('/', methods=['GET', 'POST'])
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

    return render_template("index.html",
                           title='Agenda',
                           persons=persons,
                           form=form)
