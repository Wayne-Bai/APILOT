import urllib3

# Assuming we have a proxy server details
proxy_server = 'proxy.example.com'
proxy_port = 3128

# Create a manager for the proxy server
http = urllib3.ProxyManager(f'http://{proxy_server}:{proxy_port}')

def get_server_name_and_port(url):
    # Request the server
    response = http.request('GET', url)

    # Extract the server name and port from the response headers
    server = response.headers.get('Server')

    # The server header typically includes server name and version, sometimes port
    # Parse this as necessary to get the server name and port

    # This is a placeholder solution and may not work in real situations
    # Please adjust this part according to the actual server's response header
    server_name, server_port = server.split("/")

    return (server_name.strip(), server_port.strip())
