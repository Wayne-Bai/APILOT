import urllib3

http = urllib3.PoolManager()
response = http.request('GET', 'https://example.com')

ssl_version = response.connection.sock.version
print(f"Supported SSL versions: {ssl_version}")
