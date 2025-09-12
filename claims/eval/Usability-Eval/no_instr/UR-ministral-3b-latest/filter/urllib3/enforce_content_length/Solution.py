import urllib3

# Create the HttpClient object
http = urllib3.PoolManager()

response = http.request('POST', 'http://example.com', data=b'My test', headers=None)
data = response.data  # get response data

# Now, if the 'Content-Length' header is present in the response
content_length = response.headers.get('Content-Length')

if content_length is not None:
    expected_length = int(content_length)
    if len(data) != expected_length:
        raise ValueError('The content length did not match expected length')
