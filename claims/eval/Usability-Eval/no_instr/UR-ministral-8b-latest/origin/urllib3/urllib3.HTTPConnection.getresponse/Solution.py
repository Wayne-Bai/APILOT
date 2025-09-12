import urllib3
import json

def get_server_response(url):
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    return response

url = 'https://httpbin.org/get'
server_response = get_server_response(url)

# You can handle the response further based on your needs
print(server_response)
