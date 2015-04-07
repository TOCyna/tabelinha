from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired
from flask_security.forms import RegisterForm


class InsertForm(Form):
    lastName = StringField('lastName', validators=[DataRequired()])
    firstName = StringField('firstName', validators=[DataRequired()])
    address = StringField('address', validators=[DataRequired()])
    city = StringField('city', validators=[DataRequired()])

class ExtendedRegisterForm(RegisterForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])