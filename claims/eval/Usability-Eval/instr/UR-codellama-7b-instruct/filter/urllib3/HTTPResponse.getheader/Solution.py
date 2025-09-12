
import urllib.request

# URL to send request to
url = "http://www.example.com"

# Send the request and get the response object
response = urllib.request.urlopen(url)

# Get the header values from the response
headers = response.getheader('Content-Type')
print(headers)
