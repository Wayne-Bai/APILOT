import urllib3

http = urllib3.PoolManager()

# Making a connection to a known site
response = http.request('GET', 'https://www.google.com')

# The .info() function returns a dictionary of headers
headers = response.info()

# The headers dictionary should contain a 'Server' parameter
# We'll check the value of 'Server' for the presence of 'TLS'
# This common format for saying SSL/TLS in the server's response headers
if 'TLS' in headers['Server']:
    print("Server supports SSL/TLS")
else:
    print("Server does not support SSL/TLS")
