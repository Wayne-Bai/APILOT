import urllib3

def get_lowest_supported_version():
    http = urllib3.PoolManager()
    ssl_context = http.get_ssl_context()
    return ssl_context.minimum_version

print(get_lowest_supported_version())
