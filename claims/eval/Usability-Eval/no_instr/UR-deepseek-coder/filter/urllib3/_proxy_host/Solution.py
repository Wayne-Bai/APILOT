import urllib3

def get_proxied_server_info(proxy_pass_directive):
    # Split the proxy_pass directive to extract the server name and port
    server_info = proxy_pass_directive.split("//")[1]
    server_name, port = server_info.split(":")
    
    return server_name, port

# Example usage
proxy_pass_directive = "http://example.com:8080"
server_name, port = get_proxied_server_info(proxy_pass_directive)

print(f"Server Name: {server_name}")
print(f"Port: {port}")
