import re

def parse_proxy_pass(proxy_pass):
    match = re.search('http://(.+):(\d+)', proxy_pass)
    if match is not None:
        server_name = match.group(1)
        server_port = match.group(2)
        return server_name, server_port
    else:
        return None, None

# Example usage
proxy_pass = "http://example.com:8080"
server_name, server_port = parse_proxy_pass(proxy_pass)
print(f"Server Name: {server_name}, Server Port: {server_port}")
