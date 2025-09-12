import urllib3

def get_proxy_details(proxy_url):
    # Create a PoolManager instance
    http = urllib3.PoolManager()

    # Send a request to the proxy server
    r = http.request('CONNECT', proxy_url, headers = urllib3.make_headers(proxy_basic_auth='username:password'))

    # Decode the response body
    body = r.data.decode('utf-8')

    # Parse the response body to get the server name and port
    server_name, port = body.split()[1].split(':')

    return server_name, port

# Test the function with a proxy URL
proxy_url = 'proxy.server.com:8080'
server_name, port = get_proxy_details(proxy_url)
print(f'Server Name: {server_name}, Port: {port}')
