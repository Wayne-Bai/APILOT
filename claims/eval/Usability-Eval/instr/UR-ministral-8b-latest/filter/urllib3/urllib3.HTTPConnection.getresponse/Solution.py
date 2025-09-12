import urllib3

# Create an HttpHandler object
http = urllib3.PoolManager()

# Define the URL of the server
url = 'http://example.com'  # Replace with the actual URL

try:
    # Send a GET request to the server
    response = http.request('GET', url)

    # Print the status code
    print("Status Code:", response.status)

    # Print the response data
    print("Response Data:", response.data.decode('utf-8'))

except urllib3.exceptions.RequestError as e:
    # Handle any errors that occur during the request
    print("An error occurred:", e)
