import requests
import argparse
import json

def post(addr, message):
    """The function verifies that message is a valid
       json string (and raises an Exception otherwise),
       sends the json to the given addr, gets another
       json in response, verifies that the response is
       also a valid json and prints it"""

    # TODO (using the imported functions/objects)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("addr")
    parser.add_argument("message")

    args = parser.parse_args()

    post(args.addr, args.message)
