
import urllib3

http = urllib3.PoolManager(ssl_version=ssl.PROTOCOL_TLS_CLIENT)
r = http.request('GET', 'https://www.example.com/', retries=False)
print(r.data)
