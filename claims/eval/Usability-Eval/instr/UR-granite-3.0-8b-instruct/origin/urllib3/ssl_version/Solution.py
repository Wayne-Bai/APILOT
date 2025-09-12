import urllib3

def get_supported_ssl_versions(host, port):
    http = urllib3.PoolManager()
    try:
        response = http.request('GET', f'https://{host}:{port}/ssl-versions')
        return response.data.decode()
    except Exception as e:
        return str(e)

# Usage
host = 'example.com'
port = 443
print(get_supported_ssl_versions(host, port))
