# Import the required modules from urllib3
from urllib3 import PoolManager

# Create a PoolManager object with a timeout
http = PoolManager(timeout=10.0)

# Define the URL of the server
url = "http://httpbin.org/get"

# Send a GET request to the server
try:
    response = http.request('GET', url)
    
    # Check if the request was successful
    if response.status < 400:
        print("Request successful. Status code: ", response.status)
        print("Response content: ", response.data.decode('utf-8'))
    else:
        print("Request failed. Status code: ", response.status)
except Exception as e:
    print("An error occurred: ", str(e))
