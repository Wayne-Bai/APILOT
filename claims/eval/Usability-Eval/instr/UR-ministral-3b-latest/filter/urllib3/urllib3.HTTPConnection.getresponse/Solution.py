import urllib3

# Configurate the request
http = urllib3.PoolManager()
url = "http://example.com/api"

# Send the request
response = http.request('GET', url)
print(response.data)
