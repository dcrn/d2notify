from flask import Flask, request, g, jsonify, render_template
import json, urllib.request, json, time, os

app = Flask(__name__)
poll_time = 120
last_poll = 0
items_hash = ''

@app.before_first_request
def before_first_request(*args, **kwargs):
	# Get Steam API key
	apifile = open('apikey.txt', 'r')
	g.apikey = apifile.read()

@app.route('/poll')
def poll():
	return g.apikey
	if time.time() > (last_poll + poll_time):
		# Get items file hash
		last_poll = time.time()
		return ''
	else:
		return items_hash

@app.route('/')
def index():
	return render_template('index.html')

def main():
	if not os.path.isfile('apikey.txt'):
		print('No SteamAPI key found (apikey.txt)')
	else:
		app.run(debug=True, host='0.0.0.0')

if __name__ == '__main__':
	main()
