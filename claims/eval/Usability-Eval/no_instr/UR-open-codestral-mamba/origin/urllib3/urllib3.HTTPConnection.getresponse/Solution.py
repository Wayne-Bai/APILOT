import urllib3

http = urllib3.PoolManager()  # create a pool manager for handling HTTP requests and connections

response = http.request('GET', 'http://example.com')  # send a GET request to the server

print(response.data)  # print the response data from the server
