import urllib3

# Initialize the HTTP connection pool
pool = urllib3.PoolManager()

# Example URL and http method
url = "https://httpbin.org/get"
method = "GET"

# Make HTTP request
response = pool.request(method, url)

# Print response
print(response.data)
