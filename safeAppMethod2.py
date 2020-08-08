#Extraído de: https://github.com/sqreen/DevelopersSecurityBestPractices/tree/master/_practices/timing-attack/_python

import time
from flask import Flask, request
from Crypto.Hash import HMAC, SHA256

app = Flask(__name__)

SECRET_TOKEN = 'token'

def protectedComparation(s1, s2):
    if len(s1) != len(s2):
        return False
    #Se realiza MAC en los dos token 
    h1 = HMAC.new(key=b'METODOSEGURO', msg=str.encode(s1), digestmod=SHA256)
    h2 = HMAC.new(key=b'METODOSEGURO', msg=str.encode(s2), digestmod=SHA256)
    time.sleep(0.01)
    return h1 == h2


@app.route("/")
def protected():
    token = request.headers.get('X-TOKEN')

    if not token:
        return "Missing token", 401

    if protectedComparation(token, SECRET_TOKEN):
        return "Hello admin user! Here is your secret content"
    else:
        return "WHO ARE YOU? GET OUT!", 403


if __name__ == "__main__":
    app.run()