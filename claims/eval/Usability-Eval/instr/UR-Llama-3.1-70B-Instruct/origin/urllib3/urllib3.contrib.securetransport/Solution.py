# Import the necessary libraries
import urllib3
import ssl

# Disable the NSS by NSS by setting the environment variable to 0
import os
os.environ['PYUR3_NSS'] = '0'

# Create a PoolManager that uses the default system TLS
http = urllib3.PoolManager()

# Get the list of supported TLS protocols
try:
    supported_protocols = ssl.get_supported_versions()
except AttributeError:
    # Older versions of Python don't support this call
    supported_protocols = ['TLSv1', 'TLSv1.1', 'TLSv1.2']

# Print the list of supported TLS protocols
print("Supported TLS protocols:")
for protocol in supported_protocols:
    print(protocol)

# Make a request to a website using the PoolManager
def make_request(url):
    try:
        response = http.request('GET', url)
        return response
    except urllib3.exceptions.RequestError as e:
        print("An error occurred: ", e)

# Test the make_request function
url = "https://www.example.com"
response = make_request(url)

# Check if the request was successful
if response:
    print("Request successful!")
    print("Status code: ", response.status)
    print("Headers: ", response.headers)
else:
    print("Request failed!")
