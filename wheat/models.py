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
	recipe_box = db.relationship('RecipeBox', backref='user', lazy=True)
	pantry = db.relationship('Pantry', backref='user', lazy=True)
	# meal_plans = db.relationship('Meal Plan', backref='user', lazy=True)

	def __repr__(self):
		return f"User('{self.username}', '{self.email})"


class RecipeBox(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	recipes = db.relationship('Recipe', backref='recipe_box', lazy=True)

	def __repr__(self):
		return f"Recipe Box('{self.user_id}')"

class Recipe(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	spoonacular_id = db.Column(db.Integer)
	recipe_box_id = db.Column(db.Integer, db.ForeignKey(
	    'recipe_box.id'), nullable=False)

	def __repr__(self):
		return f"Recipe('{self.spoonacular_id}')"

class Pantry(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	ingredients = db.relationship('Ingredient', backref='pantry', lazy=True)

	def __repr__(self):
		return f"Pantry('{self.id}')"

class Ingredient(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	ingredient_name = db.Column(db.String(40), nullable=False)
	pantry_id = db.Column(db.Integer, db.ForeignKey('pantry.id'), nullable=False)

	def __repr__(self):
		return f"Recipe('{self.ingredient_name}')"