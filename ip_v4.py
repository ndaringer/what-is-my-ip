import re
from flask import Flask, request, jsonify

app = Flask(__name__)

def is_ipv4(ip):
    ipv4_pattern = r"^(\d{1,3}\.){3}\d{1,3}$"
    if re.match(ipv4_pattern, ip):
        parts = ip.split(".")
        for part in parts:
            if int(part) > 255:
                return False
        return True
    return False

@app.route('/')
def get_ipv4():
    ipv4 = request.environ.get('HTTP_X_REAL_IP')
    if ipv4 and is_ipv4(ipv4):
        headers = dict(request.headers)
        return jsonify({'ipv4': ipv4, 'headers': headers})
    else:
        xff = request.environ.get('HTTP_X_FORWARDED_FOR')
        if xff:
            for ip in xff.split(','):
                ip = ip.strip()
                if is_ipv4(ip):
                    headers = dict(request.headers)
                    return jsonify({'ipv4': ip, 'headers': headers})
        headers = dict(request.headers)
        return jsonify({'ipv4': None, 'headers': headers})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
