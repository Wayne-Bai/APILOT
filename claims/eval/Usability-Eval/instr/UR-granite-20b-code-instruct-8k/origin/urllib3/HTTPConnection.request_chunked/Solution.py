import urllib3

http = urllib3.PoolManager()
response = http.request('POST', 'http://example.com/', fields={'key': 'value'})
