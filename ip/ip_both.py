from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def get_ip():
	ipv4 = request.environ.get('HTTP_X_REAL_IP')
	ipv6 = request.environ.get('HTTP_X_FORWARDED_FOR') #or request.remote_addr if no proxy

	if ipv6:
		ipv6 = ipv6.split(',')[0].strip()

	return jsonify({
		'ipv4': ipv4,
		'ipv6': ipv6,
	})

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000) #Localhost port
