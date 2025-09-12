import urllib3

# Create a PoolManager
http = urllib3.PoolManager()

# Define SSL version mapping
ssl_version_mapping = {
    'SSLv2': 'TLSv1',
    'SSLv3': 'TLSv1',
    'SSLv3.1': 'TLSv1.1',
    'TLSv1.0': 'TLSv1.0',
    'TLSv1.1': 'TLSv1.1',
    'TLSv1.2': 'TLSv1.2',
    'TLSv1.3': 'TLSv1.3'
}

def get_supported_ssl_versions():
    with http.request('GET', 'https://example.com/') as response:
        # Assuming the server gives a simple listing of supported versions
        supported_versions = response.data.decode('utf-8').split('\n')
        # Filter and map with SSL version mapping
        supported_ssl_versions = [ssl_version_mapping.get(version, '') for version in supported_versions if version in ssl_version_mapping]
        return supported_ssl_versions

print("Supported SSL Versions:", get_supported_ssl_versions())
