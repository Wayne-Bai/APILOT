
import urllib3

http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs='/path/to/ca_bundle.crt')
response = http.request('GET', 'https://www.example.com')
print(response.data)
