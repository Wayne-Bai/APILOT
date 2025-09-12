import urllib3

# Create a pool manager
http = urllib3.PoolManager()

# Function to send a request and get a response
def get_response(url):
    try:
        response = http.request('GET', url)  # Replace 'GET' with the appropriate HTTP method
        return response
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
url = 'https://example.com'
response = get_response(url)

if response is not None:
    print(f"Status Code: {response.status}")
    print(f"HTML Content: {response.data.decode('utf-8')}")
else:
    print("Failed to retrieve the response.")
