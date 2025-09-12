
import urllib3

# Creating a new PoolManager instance to avoid shared side effects
pool_manager = urllib3.PoolManager()

# Making a request using the new PoolManager instance
url = 'https://www.example.com'
response = pool_manager.request('GET', url)

print(response.data)
