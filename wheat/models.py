from datetime import datetime
from wheat import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(60), nullable=False)
	recipes = db.relationship('Recipe', backref='user', lazy=True)
	# meal_plans = db.relationship('Meal Plan', backref='user', lazy=True)

	def __repr__(self):
		return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source_url = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.source_url}')"