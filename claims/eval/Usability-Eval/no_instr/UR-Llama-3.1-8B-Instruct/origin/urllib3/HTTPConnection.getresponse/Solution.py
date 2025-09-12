 
# Import the necessary modules
from urllib import parse
from urllib3 import PoolManager
import requests

# Create a PoolManager instance
http = PoolManager()

def get_response(url):
    try:
        # Send a GET request to the provided URL
        response = http.request('GET', url)

        # Print the response status
        print("Status code: ", response.status)

        # Print the response headers
        for key, value in response.headers.items():
            print(f"{key}: {value}")

        # Print the response data
        print("Response data: ", response.data.decode('utf-8'))
        return response
    except Exception as e:
        print("An error occurred: ", e)

# Usage example
url = "http://example.com"
response = get_response(url)
