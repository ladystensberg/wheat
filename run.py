from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(60), nullable=False)
	# recipes = db.relationship('Recipe', backref='user', lazy=True)
	# meal_plans = db.relationship('Meal Plan', backref='user', lazy=True)


recipes = [
	{
		'title': 'mac & cheese',
		'desc': 'just like mom used to make!',
		'ingredients': [
			'cheese', 'noodles'
		],
		'image': 'test.jpg',
		'sourceUrl': '#',
		'kcal': 250
	},
	{
		'title': 'veggie meatballs',
		'desc': 'crispy no-meat meatballs',
		'ingredients': [
			'carrots', 'peas', 'flour'
		],
		'image': 'test.jpg',
		'sourceUrl': '#',
		'kcal': 250
	},
		{
		'title': 'mac & cheese',
		'desc': 'just like mom used to make!',
		'ingredients': [
			'cheese', 'noodles'
		],
		'image': 'test.jpg',
		'sourceUrl': '#',
		'kcal': 250
	},
	{
		'title': 'veggie meatballs',
		'desc': 'crispy no-meat meatballs',
		'ingredients': [
			'carrots', 'peas', 'flour'
		],
		'image': 'test.jpg',
		'sourceUrl': '#',
		'kcal': 250
	},
		{
		'title': 'mac & cheese',
		'desc': 'just like mom used to make!',
		'ingredients': [
			'cheese', 'noodles'
		],
		'image': 'test.jpg',
		'sourceUrl': '#',
		'kcal': 250
	},
	{
		'title': 'veggie meatballs',
		'desc': 'crispy no-meat meatballs',
		'ingredients': [
			'carrots', 'peas', 'flour'
		],
		'image': 'test.jpg',
		'sourceUrl': '#',
		'kcal': 250
	},
		{
		'title': 'mac & cheese',
		'desc': 'just like mom used to make!',
		'ingredients': [
			'cheese', 'noodles'
		],
		'image': 'test.jpg',
		'sourceUrl': '#',
		'kcal': 250
	},
	{
		'title': 'veggie meatballs',
		'desc': 'crispy no-meat meatballs',
		'ingredients': [
			'carrots', 'peas', 'flour'
		],
		'image': 'test.jpg',
		'sourceUrl': '#',
		'kcal': 250
	}
]

@app.route('/')
def home():
	# r = requests.get("https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/random?number=10&tags=vegan",
	# 	headers={"X-RapidAPI-Key": "a4d9250a03mshf716453b81f6d76p16f050jsn2669fe7fd0fb"})
	# json_resp = r.json()
	# recipes = json_resp['recipes']
	return render_template('home.html', recipes=recipes)

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'admin@blog.com' and form.password.data == 'password':
			flash('You have been logged in!', 'success')
			return redirect(url_for('home'))
		else:
			flash('Login Unsuccessful. Please check user and password.', 'danger')
	return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
	app.run(debug=True,port=5000)