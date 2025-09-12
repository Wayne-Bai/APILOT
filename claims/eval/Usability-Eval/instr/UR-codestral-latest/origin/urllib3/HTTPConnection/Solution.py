import urllib3

def create_http_connection(host, port=None, timeout=None, source_address=None, blocksize=1):
    http = urllib3.PoolManager(
        timeout=timeout,
        source_address=source_address,
        blocksize=blocksize
    )
    connection = http.connection_from_url('http://' + host + (':' + str(port) if port else ''))
    return connection

# Example usage:
host = 'example.com'
port = 8080
timeout = 5
source_address = ('localhost', 12345)
blocksize = 4096

connection = create_http_connection(host, port, timeout, source_address, blocksize)

# You can now use the 'connection' object to perform HTTP requests.
