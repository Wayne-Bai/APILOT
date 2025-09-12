import urllib3

def get_proxy_info(proxy_url):
    http = urllib3.PoolManager()
    response = http.request('GET', proxy_url)
    if response.status == 200:
        # Extract the host and port from the response
        # This is a placeholder, you need to implement the actual extraction logic
        host = response.headers['Host']
        port = response.headers['X-Forwarded-For']
        return host, port
    else:
        return None

# Usage
proxy_url = 'http://proxied_server.com:8080'
host, port = get_proxy_info(proxy_url)
if host and port:
    print(f'Host: {host}, Port: {port}')
else:
    print('Failed to get proxy information.')
