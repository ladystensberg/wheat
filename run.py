from flask import Flask, render_template, url_for
import urllib.request

app = Flask(__name__)

recipes = [
	{
		'title': 'mac & cheese',
		'desc': 'just like mom used to make!',
		'ingredients': [
			'cheese', 'noodles'
		],
		'kcal': 250
	},
	{
		'title': 'veggie meatballs',
		'desc': 'crispy no-meat meatballs',
		'ingredients': [
			'carrots', 'peas', 'flour'
		],
		'kcal': 250
	},
		{
		'title': 'mac & cheese',
		'desc': 'just like mom used to make!',
		'ingredients': [
			'cheese', 'noodles'
		],
		'kcal': 250
	},
	{
		'title': 'veggie meatballs',
		'desc': 'crispy no-meat meatballs',
		'ingredients': [
			'carrots', 'peas', 'flour'
		],
		'kcal': 250
	},
		{
		'title': 'mac & cheese',
		'desc': 'just like mom used to make!',
		'ingredients': [
			'cheese', 'noodles'
		],
		'kcal': 250
	},
	{
		'title': 'veggie meatballs',
		'desc': 'crispy no-meat meatballs',
		'ingredients': [
			'carrots', 'peas', 'flour'
		],
		'kcal': 250
	},
		{
		'title': 'mac & cheese',
		'desc': 'just like mom used to make!',
		'ingredients': [
			'cheese', 'noodles'
		],
		'kcal': 250
	},
	{
		'title': 'veggie meatballs',
		'desc': 'crispy no-meat meatballs',
		'ingredients': [
			'carrots', 'peas', 'flour'
		],
		'kcal': 250
	}
]

@app.route('/')
def hello():
	return render_template('home.html', recipes=recipes)

if __name__ == '__main__':
	app.run(debug=True,port=5000)