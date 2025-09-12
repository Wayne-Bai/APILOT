# import the urllib3 package
import urllib3

# instantiate a Pool manager
http = urllib3.PoolManager()

# specify your url
url = 'https://example.com/'

# start a HTTP request
response = http.request('GET', url)

# The response data is contained in the `data` attribute of the response item
print(response.data)
