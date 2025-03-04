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

def is_ipv6(ip):
    ipv6_pattern = r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$"
    return re.match(ipv6_pattern, ip)

@app.route('/')
def get_ip():
    ipv4 = None
    ipv6 = None

    xff = request.environ.get('HTTP_X_FORWARDED_FOR')
    if xff:
        for ip in xff.split(','):
            ip = ip.strip()
            if is_ipv4(ip):
                if ipv4 is None:
                    ipv4 = ip
            elif is_ipv6(ip):
                if ipv6 is None:
                    ipv6 = ip

    headers = dict(request.headers) #Get all headers.

    return jsonify({
        'ipv4': ipv4,
        'ipv6': ipv6,
        'headers': headers,
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
