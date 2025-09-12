import urllib3

http = urllib3.PoolManager()

context = ssl.create_default_context(cafile='ca-bundle.crt')
context.check_hostname = True
context.verify_mode = ssl.CERT_REQUIRED

http.request('GET', 'https://www.example.com', headers={'Host': 'www.example.com'}, connect_timeout=5, timeout=5)

response = http.get_response()
data = response.read()

print(data)
