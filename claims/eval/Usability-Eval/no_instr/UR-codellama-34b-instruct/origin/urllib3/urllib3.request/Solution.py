
import urllib3

# Create a new PoolManager instance to avoid side effects from shared dependencies
with urllib3.PoolManager() as http:
    # Use the convenience request method, but specify the PoolManager instance explicitly
    response = http.request('GET', 'https://httpbin.org/get')
    print(response.status_code)
