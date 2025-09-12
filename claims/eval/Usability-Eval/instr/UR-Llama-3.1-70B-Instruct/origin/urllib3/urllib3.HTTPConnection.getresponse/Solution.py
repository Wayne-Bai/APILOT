# Import the urllib3 library
import urllib3

# Create a PoolManager instance
http = urllib3.PoolManager()

# Define the URL you want to send the request to
url = "http://httpbin.org/anything"

# Send a GET request to the server
response = http.request('GET', url)

# Check if the request was successful
if response.status == 200:
    # Get the response from the server
    data = response.data.decode('utf-8')
    print("Response from the server:", data)
else:
    print("Failed to get response from the server.")
    print("Status code:", response.status)
    print("Reason:", response.reason)
