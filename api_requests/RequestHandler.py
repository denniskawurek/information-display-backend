import requests
import config

JSON_HEADER = {"Content-Type": "application/json"}
SERVER_URL = "http://localhost:5000/" # url of flask api

''' This class sends requests to the FLASK server '''
class RequestHandler():
    def get(self, path):
        return requests.get(SERVER_URL + path)

    def put(self, path, jsonData):
        r = requests.put(SERVER_URL + path, headers=JSON_HEADER, json=jsonData)
        if r.status_code is not 200:
            print("Error in PUT request")
            print(r.text)

    def post(Self, path, jsonData):
        r = requests.post(SERVER_URL + path, headers=JSON_HEADER, json=jsonData)
        if r.status_code is not 200:
            print("Error in POST request")
            print(r.text)
