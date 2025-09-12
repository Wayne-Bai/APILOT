import urllib3

# Create a connection pool manager
http = urllib3.PoolManager()

# Specify the proxy URL
proxy_url = 'http://proxyserver.example.com:3128/'

# Define the URL of the resource you want to fetch
target_url = 'http://httpbin.org/ip'

# Set up the proxy by specifying the 'http' and 'https' paths in the proxy dictionary
proxy = urllib3.ProxyManager(proxy_url)

# Use the proxy to make a request to the target URL
response = proxy.request('GET', target_url)

# Print response data
print("Response Status:", response.status)
print("Response Data:", response.data.decode('utf-8'))
