import urllib3

def get_supported_ssl_versions(host, port):
    http = urllib3.PoolManager()
    response = http.request('GET', f'https://{host}:{port}/')
    # Assuming the server responds with a JSON containing the supported SSL versions
    # Replace the following line with the actual parsing logic based on the server's response
    supported_ssl_versions = response.data.decode().split('(')[1].split(')')[0].split(',')
    return supported_ssl_versions

# Usage
host = 'example.com'
port = 443
supported_ssl_versions = get_supported_ssl_versions(host, port)
print(supported_ssl_versions)
