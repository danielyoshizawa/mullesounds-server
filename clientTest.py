import requests
import json


def post(payload):
    url = "http://localhost:4000/jsonrpc"
    headers = {'content-type': 'application/json'}

    return requests.post(url, data=json.dumps(payload), headers=headers).json()

def main():
    payload = {
        "method" : "soundList",
        "params" : [],
        "jsonrpc" : "2.0",
        "id" : 1,
        }

    response = post(payload)

    print(response)

    soundList = response["result"]
    print(soundList)

    for sound in soundList["sounds"]:
        print(sound["Filename"])
        payload = {
            "method": "play",
            "params": [sound["Filename"]],
            "jsonrpc": "2.0",
            "id": 2,
            }

        response = post(payload)

if __name__ == "__main__":
    main()
