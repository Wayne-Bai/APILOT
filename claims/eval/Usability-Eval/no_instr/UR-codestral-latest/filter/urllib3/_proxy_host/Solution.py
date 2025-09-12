import urllib.parse

# A sample proxy_pass directive
proxy_pass_directive = "http://example.com:8080/path"

# Parse the URL
parsed_url = urllib.parse.urlparse(proxy_pass_directive)

# Extract the hostname and port
hostname = parsed_url.hostname
port = parsed_url.port

print(f"Hostname: {hostname}, Port: {port}")
