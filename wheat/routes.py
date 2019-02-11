from flask import render_template, url_for, flash, redirect
from wheat import app
from wheat.forms import RegistrationForm, LoginForm
from wheat.models import User, Recipe
from flask_login import login_user, current_user, logout_user, login_required
import requests

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