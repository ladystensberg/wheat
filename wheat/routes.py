from flask import render_template, url_for, flash, redirect, request
from wheat import app, db, bcrypt
from wheat.forms import RegistrationForm, LoginForm, AddToPantry
from wheat.models import User, Recipe, Ingredient
from flask_login import login_user, current_user, logout_user, login_required
import requests

recipes = [
	{
		'spoonacular_id': 5
	},
	{
		'spoonacular_id': 105
	},
	{
		'spoonacular_id': 35
	},
	{
		'spoonacular_id': 485
	}
]

@app.route('/')
def home():
	#params for request URL
	results = "10"
	tags = "vegan"

	r = requests.get(f"https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/random?number={results}&tags={tags}",
		headers={"X-RapidAPI-Key": "a4d9250a03mshf716453b81f6d76p16f050jsn2669fe7fd0fb"})
	json_resp = r.json()
	recipes = json_resp['recipes']
	return render_template('home.html', recipes=recipes)

@login_required
@app.route('/recipes')
def get_recipes():
	ingredients = Ingredient.query.filter_by(user=current_user).all()
	ingredients_list = []
	for ingredient in ingredients:
		ingredients_list.append(ingredient.ingredient_name)
	
	# params for request URL
	joined_list = ','.join(ingredients_list)
	diet = "vegan"
	type = "main course" # options: main course, side dish, dessert, appetizer, salad, bread, breakfast, soup, beverage, sauce, or drink.
	ranking = "0" # Whether to minimize missing ingredients (0), maximize used ingredients (1) first, or rank recipes by relevance (2).
	fill_ingredients = "true" # Add information about the used and missing ingredients in each recipe.
	add_recipe_info = "true" # BOOLEAN, true returns more info about the recipe
	limit_license = "true"
	offset = "0" # number of results to skip, 0-900
	results = "20" # number of results to return, 0-100

	r = requests.get(f"https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/searchComplex?type={type}&diet={diet}&includeIngredients={joined_list}&ranking={ranking}&fillIngredients={fill_ingredients}&addRecipeInformation={add_recipe_info}&limitLicense={limit_license}&offset={offset}&number={results}",
		headers={"X-RapidAPI-Key": "a4d9250a03mshf716453b81f6d76p16f050jsn2669fe7fd0fb"})
	json_resp = r.json()
	recipes = json_resp['results']
	print(recipes)
	return render_template('recipes.html', recipes=recipes)

@login_required
@app.route('/recipes/<int:recipe_id>')
def get_single_recipe(recipe_id):
	r = requests.get(f"https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/{recipe_id}/information",
		headers={"X-RapidAPI-Key": "a4d9250a03mshf716453b81f6d76p16f050jsn2669fe7fd0fb"})
	json_resp = r.json()
	recipe = json_resp
	print(recipe)
	return render_template('recipe.html', recipe=recipe)

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