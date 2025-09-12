import urllib3

# Define the proxy server address and port
proxy_host = 'your_proxy_host'  # Replace with your proxy host
proxy_port = 8080                # Replace with your proxy port

# Create a PoolManager with the proxy settings
http = urllib3.ProxyManager(f'http://{proxy_host}:{proxy_port}')

# Now you can use `http` to make requests through the proxy
response = http.request('GET', 'http://example.com')

# Print response data
print(response.data)
