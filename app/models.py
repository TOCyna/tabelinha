from app import db

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lastName = db.Column(db.String(255), index=True)
    firstName = db.Column(db.String(255), index=True)
    address = db.Column(db.String(255), index=True)
    city = db.Column(db.String(255), index=True)

    def __repr__(self):
        return '<Person %r>' % (self.lastName)