from flask import Flask, render_template, url_for
import urllib.request
import requests

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
	r = requests.get('https://www.food2fork.com/api/search?key=4c35304520e416705a32ee2cc96ccb1d')
	json_resp = r.json()
	recipes = json_resp['recipes']
	return render_template('home.html', recipes=recipes)

if __name__ == '__main__':
	app.run(debug=True,port=5000)