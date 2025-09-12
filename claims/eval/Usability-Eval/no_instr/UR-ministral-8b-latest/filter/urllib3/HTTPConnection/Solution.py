import urllib3

# Create an HTTPConnection
http = urllib3.HTTPConnection(
    host='example.com',
    port=80,
    timeout=30,
    source_address=('localhost', 1234)
)

# Use the HTTPConnection instance to send a request
response = http.request('GET', '/', httplib=urllib3.EventHttpConnection())
print(response.data.decode('utf-8'))
