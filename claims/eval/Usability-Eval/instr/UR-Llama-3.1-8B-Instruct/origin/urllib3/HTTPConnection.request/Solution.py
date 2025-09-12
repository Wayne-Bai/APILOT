# Importing the required libraries
import urllib3
import sys

# Create an instance of the HTTP client using PoolManager from the urllib3 library
http = urllib3.PoolManager()

# Define the HTTP request method and the request URI
http_method = "GET"  # Change to the required HTTP method
url = "http://example.com"  # Change to the required URL

# Construct the request using the http request method and the request URI
if http_method == "OPTIONS":
    request = http.request("OPTIONS", url)
elif http_method == "CONNECT":
    request = http.request("CONNECT", url)
else:
    request = http.request(http_method, url)

# Print the response from the server
print("Response Status: ", request.status)
print("Response Reason: ", request.reason)
print("Response Headers: ", request.headers)
print("Response Body: ", request.data)

# Disable the ssl verification to avoid certificate verification errors
# if not http.retriesistrict_ssl_validation:
#     http.check_CERT = False
