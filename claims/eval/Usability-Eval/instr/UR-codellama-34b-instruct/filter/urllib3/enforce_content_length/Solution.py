import urllib3

# Set up the HTTP request
http = urllib3.PoolManager()
request = http.request('GET', 'https://www.example.com')

# Check if the Content-Length header is present in the response
if 'Content-Length' in request.headers:
    # Get the value of the Content-Length header
    content_length = int(request.headers['Content-Length'])

    # Compare the length of the body with the value of the Content-Length header
    if len(request.data) != content_length:
        raise ValueError('Body returned by server does not match Content-Length header')
else:
    print('No Content-Length header present in response')
