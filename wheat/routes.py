from flask import render_template, url_for, flash, redirect, request
from wheat import app, db, bcrypt
from wheat.forms import RegistrationForm, LoginForm, AddToPantry
from wheat.models import User, Recipe, Ingredient
from flask_login import login_user, current_user, logout_user, login_required
import requests

recipes = [
	{
		'image': 'image',
		'title': 'Vegan Mac'
	},
	{
		'image': 'image',
		'title': 'Vegan Mac'
	},
	{
		'image': 'image',
		'title': 'Vegan Mac'
	},
	{
		'image': 'image',
		'title': 'Vegan Mac'
	},
]

@app.route('/')
def home():
	#TODO: Come up with new place for homepage
	return render_template('home.html', recipes=recipes)

@login_required
@app.route('/recipes')
def get_recipes():
	ingredients = Ingredient.query.filter_by(user=current_user).all()
	ingredients_list = []
	for ingredient in ingredients:
		ingredients_list.append(ingredient.ingredient_name)
	joined_list = ','.join(ingredients_list)
	
	health_labels = "vegan" # diet
	api_id = "11066273"
	api_key = "49d61e99071532d1650fdd122a74d07b"
	search_term = "" #currently using ingredients but can enter other things here instead
	first_result = "0"
	last_result = "20"
	excluded_ingredients = ""
	
	r = requests.get(f"https://api.edamam.com/search?q={joined_list}&app_id={api_id}&app_key={api_key}&from={first_result}&to={last_result}&health={health_labels}")
	json_resp = r.json()
	recipes = json_resp['hits']
	return render_template('recipes.html', recipes=recipes)

@app.route("/register", methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data, email=form.email.data, password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash('Your account has been created! You are now able to log in', 'success')
		return redirect(url_for('login'))
	return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('account'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
	form = AddToPantry()
	if form.validate_on_submit():
		ingredient = Ingredient(ingredient_name=form.ingredient_name.data, user=current_user)
		db.session.add(ingredient)
		db.session.commit()
		return redirect(url_for('account'))
	return render_template('account.html', title='Account', form=form)

@app.route("/ingredient/<int:ingredient_id>/delete", methods=['POST'])
@login_required
def delete_ingredient(ingredient_id):
	ingredient = Ingredient.query.get(ingredient_id)
	if ingredient.user != current_user:
		print("error") #TODO
	db.session.delete(ingredient)
	db.session.commit()
	flash(f"{ingredient.ingredient_name} has been deleted", 'success')
	return redirect(url_for('account'))