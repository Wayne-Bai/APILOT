
# Importing the required urllib3 library
import urllib3

# URL of the proxied server
proxied_server_url = 'http://example.com'
# Extracting server name and port from the URL in case needed
server_name = urllib3.util.parse_url(proxied_server_url).host
server_port = urllib3.util.parse_url(proxied_server_url).port

print("Server Name:", server_name)
print("Server Port:", server_port)
