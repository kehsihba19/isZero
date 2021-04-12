import requests
from flask import Flask ,render_template, request,jsonify

app = Flask(__name__)

def check_zero(word):
	isZero=False
	BASE_URL="https://api.adviceslip.com/advice"
	joke=requests.get(BASE_URL).json()
	if(word.count('0')==len(word)):
		isZero=True
	elif(word.count('.')==1 and (word.count('0')+1)==len(word)):
		isZero=True
	elif(word.lower()=='zero'):
		isZero=True
	return {'ad':joke['slip']['advice'],'isZero':isZero}

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/api/<word>')
def api(word):
	data = check_zero(word)
	return jsonify(data)

if __name__ == "__main__":
    #app.debug = True
    app.run()