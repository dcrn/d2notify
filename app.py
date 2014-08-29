from flask import Flask, request, g, jsonify, render_template
import json, urllib.request, json, time, os

app = Flask(__name__)
apikey = ''
poll_time = 120
last_poll = 0
items_hash = ''

@app.before_first_request
def before_first_request(*args, **kwargs):
	# Get Steam API key
	global apikey
	apifile = open('apikey.txt', 'r')
	apikey = apifile.read()

	# Get current item hash
	poll()

@app.route('/poll')
def poll():
	global apikey, last_poll, poll_time, items_hash

	if time.time() > (last_poll + poll_time):
		last_poll = time.time()
		jdata = ''
		try:
			jdata = urllib.request.urlopen('http://api.steampowered.com/IEconItems_570/GetSchemaURL/v1?key=' + apikey).read()
		except:
			return ''

		j = json.loads(str(jdata, 'UTF-8'))
		items_hash = j['result']['items_game_url'][-44:-4]
	
	return items_hash

@app.route('/')
def index():
	global items_hash
	return render_template('index.html', hash=items_hash)

def main():
	if not os.path.isfile('apikey.txt'):
		print('No SteamAPI key found (apikey.txt)')
	else:
		app.run(host='0.0.0.0')

if __name__ == '__main__':
	main()
