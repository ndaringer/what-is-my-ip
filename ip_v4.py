from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def get_ipv4():
	ipv4 = request.environ.get('HTTP_X_REAL_IP')

	return jsonify({
		'ipv4': ipv4,
	})

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5001) #Different port
