import urllib3

http = urllib3.PoolManager()

response = http.request('GET', 'https://example.com/foo', return_path_data=False)
