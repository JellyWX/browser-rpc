from flask import Flask, request, abort
import json

app = Flask(__name__)

held = {}

@app.route('/', methods=['POST', 'GET'])
def update():
    if request.method == 'GET':
        if request.headers['email'] in held.keys():
            return json.dumps(held[request.headers['email']])
        else:
            abort(404)

    elif request.method == 'POST':
        print(request.json)

        held[request.headers['email']] = request.json

        return ''

if __name__ == '__main__':
    app.run(debug=True, host='jellywx.co.uk', ssl_context=('/etc/letsencrypt/live/jellywx.co.uk/fullchain.pem', '/etc/letsencrypt/live/jellywx.co.uk/privkey.pem'))
