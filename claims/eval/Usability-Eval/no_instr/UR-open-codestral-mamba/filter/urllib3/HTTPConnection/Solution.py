import urllib3

http = urllib3.PoolManager()

# Make a GET request
response = http.request('GET', 'http://example.com/')

print(response.data)  # print the response body
