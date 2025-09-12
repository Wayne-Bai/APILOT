
import urllib3

# Set up the URL for the proxied server
proxied_server_url = 'http://example.com'

# Set up the URL for the proxy server
proxy_server_url = 'http://proxy.com'

# Create a connection to the proxy server using urllib3
proxy_conn = urllib3.ProxyManager(proxied_server_url, proxy_server_url)

# Send a GET request to the proxied server
response = proxy_conn.request('GET', '/')

print(response.data)
