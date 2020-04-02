from flask import Flask
from flask import request
from flask import abort

app = Flask(__name__)


@app.route('/', methods=['GET'])
def Hello_api():
    name = request.args.get("name")
    if name is None:
        abort(418)
    return Hello(name)


def Hello(name):
    return f'Hello, {name}!'
