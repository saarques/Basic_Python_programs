from flask import Flask, jsonify, make_response, request

import keras
app = Flask(__name__)

@app.route('/')
def hello_world():
	value = "Hello World! \n This is a demo bitch, wait for the content. :)"
	return value


@app.route('/value', methods = ["GET"])
def bringit():
	if request.method == 'GET':
		string = input("Enter address of image: ")
		string = str(string) + " VOILA!"
		return jsonify(string)

@app.route('/predict', methods = ["POST"])
def predict():
	try:
		if "address" in request.get_json():
			data = request.get_json()['address']
			return jsonify(str(data) + ".bmp")
	except KeyError:
		return jsonify("Provide a proper value for address!")


if __name__ == '__main__':
	app.run(debug = True)