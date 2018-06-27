import requests
import argparse
import json

def post(addr, message):
    response = requests.post(addr, json=json.loads(message))
    print(response.json())

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("addr")
    parser.add_argument("message")

    args = parser.parse_args()

    post(args.addr, args.message)
