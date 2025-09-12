import urllib3

# Create a proxied HTTP connection using urllib3
http = urllib3.PoolManager()

# Specify the proxied server's name and port
proxy_name = 'example-proxy'
proxy_port = 8080

# Configure the proxied server in the PoolManager
http.proxy = proxies = {
    'http': f'{proxy_name}:{proxy_port}',
    'https': f'{proxy_name}:{proxy_port}'
}

# Define a URL to send a request to
url = 'http://example.com'

# Send a request to the specified URL through the proxied server
response = http.request('GET', url)

# Print the response
print(response.data.decode('utf-8'))
