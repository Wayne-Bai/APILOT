# Import the necessary libraries
import urllib3

# Create a http client instance
http = urllib3.HTTPSConnectionPool(host='example.com', port=443)

# Send a request to the server
response = http.request('GET', '/path/to/resource')

# Get the response from the server
# http_response is the argument if a value is passed.
def get_response(http_response = None):
    if http_response:
        return http_response
    else:
        http.close()
        return response

response = get_response()
print(response.status)
print(response.data.decode('utf-8'))
