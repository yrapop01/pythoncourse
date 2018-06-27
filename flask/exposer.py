from flask import Flask, request, jsonify
from rpc import expose
import json

app = Flask(__name__)

@expose(app)
def n(a, b, n=16):
    return a * b + n

if __name__ == "__main__":
    app.run()
