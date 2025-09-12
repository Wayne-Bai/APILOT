import requests
import json

url = 'http://example.com'
headers = {'Content-Type': 'application/json'}
data = {'key': 'value'}

def generate_request_body():
    for chunk in json.JSONEncoder().iterencode(data):
        yield chunk

response = requests.post(url, headers=headers, data=generate_request_body())
