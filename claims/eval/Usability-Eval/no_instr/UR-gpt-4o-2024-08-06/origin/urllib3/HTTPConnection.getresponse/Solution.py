import urllib3

# Create a PoolManager instance to manage connections
http = urllib3.PoolManager()

# Make a request to a URL
url = "http://httpbin.org/get"
response = http.request('GET', url)

# Print the status and data from the response
print("Status:", response.status)
print("Data:", response.data.decode('utf-8'))
