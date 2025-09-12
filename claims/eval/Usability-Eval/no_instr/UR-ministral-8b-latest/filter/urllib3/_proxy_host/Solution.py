import urllib3

# Define the proxied server details
proxy_host = "your_proxy_host"
proxy_port = "your_proxy_port"

# Create a pool manager with the proxy settings
http = urllib3.PoolManager(proxy_url=f"http://{proxy_host}:{proxy_port}")

# Resource URL to be accessed through the proxy
url = "http://example.com"

# Make a request to the resource URL using the proxy
response = http.request("GET", url)

# Print the response
print(response.data.decode('utf-8'))
