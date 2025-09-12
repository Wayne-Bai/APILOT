import urllib3

# Create a pool manager
http = urllib3.PoolManager()

# Set the proxy details
proxy_host = "proxy.example.com"
proxy_port = 8080

# Create a proxy URL
proxy_url = f"http://{proxy_host}:{proxy_port}/"

# Create a pool manager with proxy settings
proxy = urllib3.ProxyManager(proxy_url)

# Use the ProxyManager to make a request
url = "http://example.com"
response = proxy.request('GET', url)

# Print the status and data
print('Status:', response.status)
print('Data:', response.data.decode('utf-8'))
