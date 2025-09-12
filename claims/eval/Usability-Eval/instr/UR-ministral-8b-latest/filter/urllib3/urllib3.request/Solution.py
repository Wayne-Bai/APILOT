import urllib3

def get_request(url, **kwargs):
    pool_manager = urllib3.PoolManager()
    response = pool_manager.request('GET', url, **kwargs)
    return response

# Example usage
response = get_request('https://api.example.com/data', headers={'Authorization': 'Bearer token'})
print(response.status)
print(response.data)
