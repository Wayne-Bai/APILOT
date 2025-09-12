import urllib3

http = urllib3.PoolManager()

# Assuming the endpoint is https://api.example.com/data
# And the task is to get data from this endpoint
r = http.request('GET', 'https://api.example.com/data')

# Print the status, headers, and data
print(r.status)  # prints the status code
print(r.headers)  # prints the headers
print(r.data)  # prints the data
