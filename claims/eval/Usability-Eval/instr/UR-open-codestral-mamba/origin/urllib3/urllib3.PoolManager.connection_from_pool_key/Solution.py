import urllib3

# Create a connection pool manager
http = urllib3.PoolManager()

# Assuming 'pool_key' is the key you have
pool_key = 'your_key'
response = http.request('GET', f'http://{pool_key}.com/')

# You can now use 'response' to get the data, for example, as text:
data = response.data
print(data)
