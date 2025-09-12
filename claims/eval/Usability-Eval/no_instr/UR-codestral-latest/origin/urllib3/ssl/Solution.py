import urllib3

# Create a pool manager instance for sending requests.
http = urllib3.PoolManager()

# Make a GET request to the URL.
r = http.request('GET', 'https://www.example.com')

# Print the status of the response.
print(f'The status code is: {r.status}')

# Print the data received from the server.
print(r.data)
