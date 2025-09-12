import urllib3
http = urllib3.HTTPConnection('www.google.com', timeout=10, source_address=('127.0.0.1', 8080))
http.request('GET', '/')
r = http.getresponse()
print(r.read())
