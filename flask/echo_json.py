from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def echo():
    data = request.get_json(silent=True)
    return jsonify(data)

if __name__ == "__main__":
    app.run()
