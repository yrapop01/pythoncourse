from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def echo():
    """This function gets a json from the client,
       verifies that it is a valid json (and raises
       an exception otherwise) and sends this json
       in response"""

    # TODO (using the imported functions/objects)

if __name__ == "__main__":
    app.run()
