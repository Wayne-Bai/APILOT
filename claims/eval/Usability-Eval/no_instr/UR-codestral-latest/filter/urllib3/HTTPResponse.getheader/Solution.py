import urllib.request

# Make a request to the URL
response = urllib.request.urlopen('http://example.com')

# Get the header value (replace 'Your-Header' with the actual header name)
header_value = response.getheader('Your-Header')

print('The value of the header is:', header_value)
