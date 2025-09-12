import urllib3

# Create a new PoolManager instance
http = urllib3.PoolManager()

# Function to make a request
def make_request(url):
    try:
        response = http.request('GET', url)
        return response.data
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
