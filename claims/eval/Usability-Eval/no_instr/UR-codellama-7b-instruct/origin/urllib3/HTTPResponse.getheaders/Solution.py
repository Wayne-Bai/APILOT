import urllib3

# Create a HTTP client object
http = urllib3.PoolManager()

# Get the headers for a given URL
headers = http.request('GET', 'https://www.example.com').headers

# Print the headers and their values
print(headers)
