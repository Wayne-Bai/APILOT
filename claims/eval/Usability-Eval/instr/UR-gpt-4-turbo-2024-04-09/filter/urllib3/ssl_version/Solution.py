import urllib3
from urllib3.util.ssl_ import create_urllib3_context

# List of SSL versions to test
ssl_versions = [
    "SSLv23",
    "TLSv1",
    "TLSv1_1",
    "TLSv1_2",
    "TLSv1_3"
]

def check_ssl_versions(url):
    http = urllib3.PoolManager()
    for version in ssl_versions:
        try:
            # Creating SSL context for a specific SSL version
            context = create_urllib3_context(ssl_version=version)
            # Using the context in a connection
            http.connection_pool_kw['ssl_context'] = context
            response = http.request('GET', url)
            
            # If the request does not raise an error, the SSL version is supported
            print(f"{version}: Supported")
        except urllib3.exceptions.SSLError as e:
            # If an SSL error occurs, the SSL version is not supported
            print(f"{version}: Not supported - SSL error")
        except Exception as e:
            # General exception handling (e.g., network issues)
            print(f"{version}: Not supported - {str(e)}")

# Example usage
url = "https://www.example.com"
check_ssl_versions(url)
