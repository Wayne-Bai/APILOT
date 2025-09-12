import urllib3

# Specify the proxy URL
proxy_url = 'http://your-proxy-server.com:port'

# Create a ProxyManager instance with the given proxy URL
http = urllib3.ProxyManager(proxy_url)

# Your target URL to which the request will be made through the proxied server
url = 'http://example.com/'

# Making a GET request through the proxy
response = http.request('GET', url)

# Print the response
print(response.data)
