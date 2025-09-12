import urllib3

def get_proxy_info(proxy_pass):
    http = urllib3.PoolManager()
    response = http.request('GET', proxy_pass)
    if response.status == 200:
        proxy_info = response.headers.get('Proxy-Info')
        if proxy_info:
            return proxy_info.split(':')
        else:
            return None
    else:
        return None

# Example usage:
proxy_pass = 'http://example.com/proxy_pass'
proxy_info = get_proxy_info(proxy_pass)
if proxy_info:
    print(f'Proxy Name: {proxy_info[0]}')
    print(f'Proxy Port: {proxy_info[1]}')
else:
    print('No proxy information found.')
