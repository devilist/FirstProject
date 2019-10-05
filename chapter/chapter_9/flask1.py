import flask
from flask import Flask, render_template

app = Flask(__name__, static_folder='.', static_url_path='')


@app.route('/')
def home():
	return app.send_static_file('index.html')


@app.route('/echo/<thing>')
def echo(thing):
	return "say hello to my little friend: %s!" % thing


@app.route('/echo1/<thing>')
def echo1(thing):
	return render_template('flask1.html', thing=thing)


app.run(port=9999, debug=True)
