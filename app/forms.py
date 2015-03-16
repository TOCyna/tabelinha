from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class InsertForm(Form):
    lastName = StringField('lastName', validators=[DataRequired()])
    firstName = StringField('firstName', validators=[DataRequired()])
    address = StringField('address', validators=[DataRequired()])
    city = StringField('city', validators=[DataRequired()])