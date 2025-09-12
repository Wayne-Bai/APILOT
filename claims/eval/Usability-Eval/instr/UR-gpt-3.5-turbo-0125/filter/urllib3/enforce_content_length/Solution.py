
import urllib3
from urllib3.exceptions import ProtocolError

http = urllib3.PoolManager()

url = 'http://www.example.com/'
response = http.request('GET', url)

content_length = response.headers.get('content-length')
if content_length:
    expected_length = int(content_length)
    actual_length = len(response.data)
    if expected_length != actual_length:
        raise ProtocolError('Content length mismatch. Expected {}, but received {}.'.format(expected_length, actual_length))
else:
    raise ProtocolError('Content-Length header not found in response.')
