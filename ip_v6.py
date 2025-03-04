import re
from flask import Flask, request, jsonify

app = Flask(__name__)

def is_ipv6(ip):
    ipv6_pattern = r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$"
    return re.match(ipv6_pattern, ip)

@app.route('/')
def get_ipv6():
    ipv6 = None

    xff = request.environ.get('HTTP_X_FORWARDED_FOR')
    if xff:
        for ip in xff.split(','):
            ip = ip.strip()
            if is_ipv6(ip):
                if ipv6 is None:
                    ipv6 = ip

    headers = dict(request.headers)
    return jsonify({'ipv6': ipv6, 'headers': headers})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
