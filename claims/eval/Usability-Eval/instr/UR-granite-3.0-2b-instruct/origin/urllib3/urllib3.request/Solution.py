from urllib3 import PoolManager

# Create a new PoolManager instance
pool = PoolManager()

# Define a function to make requests
def make_request(method, url, **kwargs):
    with pool.request(method, url, **kwargs) as response:
        return response
