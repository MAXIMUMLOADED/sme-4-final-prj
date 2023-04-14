# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from IP import tesseract

# creating a Flask app
app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.

@app.route('/getdata', methods = ['GET', 'POST'])
def home():
	if(request.method == 'GET'):

		data = tesseract()
        
		return jsonify({'data': data})



# driver function
if __name__ == '__main__':

	app.run(debug = True)
 
