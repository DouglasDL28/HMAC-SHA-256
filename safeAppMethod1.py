#Extraído de: https://github.com/sqreen/DevelopersSecurityBestPractices/tree/master/_practices/timing-attack/_python

import time
from flask import Flask, request

app = Flask(__name__)

SECRET_TOKEN = 'token'

def protectedComparation(s1, s2):
    if len(s1) != len(s2):
        return False

    res = 0
    for c1, c2 in zip(s1, s2):
        c1 = ord(c1)
        c2 = ord(c2)
        res |= c1 ^ c2 
        time.sleep(0.01)
    return res == 0


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