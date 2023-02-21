from flask import Flask, jsonify, after_this_request,request
import random, string

app = Flask(__name__)

@app.route('/')
def hello():
	
	@after_this_request
	def add_header(response):
		response.headers.add('Access-Control-Allow-Origin', '*')
		return response
	
	couponCode = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(10))
	args = request.args

	jsonResp = {'couponCode': couponCode}
	return jsonify(jsonResp)

if __name__ == "__main__":
    app.run()