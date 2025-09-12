import urllib3

http = urllib3.PoolManager()
response = http.request('GET', 'https://example.com')

if response.headers['ssl-version'] in ['TLSv1.2', 'TLSv1.3']:
    print('Supported SSL version: {}'.format(response.headers['ssl-version']))
else:
    print('Unsupported SSL version')
