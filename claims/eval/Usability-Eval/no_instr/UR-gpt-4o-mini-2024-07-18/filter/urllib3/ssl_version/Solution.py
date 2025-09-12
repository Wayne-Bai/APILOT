import urllib3
from urllib3.util import ssl_

# Function to check supported SSL versions
def check_ssl_versions(url):
    http = urllib3.PoolManager()
    try:
        response = http.request('GET', url)
        ssl_info = ssl_.get_https_context(http.connection_pool.key).options
        supported_versions = []
        
        if ssl_info & ssl_.SSLContextOptions.SSLv23:
            supported_versions.append('SSLv23')
        if ssl_info & ssl_.SSLContextOptions.TLSv1:
            supported_versions.append('TLSv1')
        if ssl_info & ssl_.SSLContextOptions.TLSv1_1:
            supported_versions.append('TLSv1.1')
        if ssl_info & ssl_.SSLContextOptions.TLSv1_2:
            supported_versions.append('TLSv1.2')
        if ssl_info & ssl_.SSLContextOptions.TLSv1_3:
            supported_versions.append('TLSv1.3')

        print(f"Supported SSL versions for {url}: {supported_versions}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
check_ssl_versions('https://example.com')
