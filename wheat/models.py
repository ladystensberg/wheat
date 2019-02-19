from datetime import datetime
from wheat import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(60), nullable=False)
	recipes = db.relationship('Recipe', backref='user', lazy=True)
	pantry_items = db.relationship('Ingredient', backref='user', lazy=True)
	# meal_plans = db.relationship('Meal Plan', backref='user', lazy='dynamic')

	def __repr__(self):
		return f"User('{self.username}', '{self.email})"

class Recipe(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	spoonacular_id = db.Column(db.Integer)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def __repr__(self):
		return f"Recipe('{self.spoonacular_id}')"

class Ingredient(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	ingredient_name = db.Column(db.String(40), nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def __repr__(self):
		return f"Ingredient('{self.ingredient_name}')"