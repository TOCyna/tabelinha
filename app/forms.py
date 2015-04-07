from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, IntegerField, DateField
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
    address = StringField('Address', validators=[DataRequired()])
    number = StringField('Number', validators=[DataRequired()])
    address2 = StringField('Address2')
    neighbourhood = StringField('Neighbourhood', validators=[DataRequired()])
    zipcode = StringField('Zipcode', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    birthday = DateField('Birthday', validators=[DataRequired()], format='%d-%m-%Y')
    cellphone = StringField('Celllphone', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])