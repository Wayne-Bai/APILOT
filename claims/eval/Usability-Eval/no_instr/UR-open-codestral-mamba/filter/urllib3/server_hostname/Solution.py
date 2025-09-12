import urllib3

# create a pool manager
http = urllib3.PoolManager()

# specify the URL
url = "http://example.com"

# make a GET request to the URL
response = http.request('GET', url)

# print the status code of the response
print(response.status)

# print the data of the response
print(response.data)
