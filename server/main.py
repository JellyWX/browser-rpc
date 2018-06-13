from flask import Flask, request

app = Flask(__name__)

held = {}

@app.route('/', methods=['POST', 'GET'])
def update():
    if request.method == 'GET':
        return held.pop(request.headers['email'])

    elif request.method == 'POST':
        held[request.headers['email']] = request.json

        return ''
