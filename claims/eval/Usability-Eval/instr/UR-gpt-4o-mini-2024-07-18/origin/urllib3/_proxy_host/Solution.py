import urllib3

# Define the proxy server details
proxy_url = "http://your-proxy-server:port"  # Replace with your proxy server URL and port

# Create a ProxyManager for making requests through the proxy
http = urllib3.ProxyManager(proxy_url)

# Example of making a GET request through the proxy
response = http.request('GET', 'http://example.com')

# Print the response data
print(response.data.decode('utf-8'))
