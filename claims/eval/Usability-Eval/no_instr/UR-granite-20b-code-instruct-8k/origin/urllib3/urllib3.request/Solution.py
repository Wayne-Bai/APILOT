import urllib3
http = urllib3.PoolManager()

# Use the 'request' method of the 'http' object to send a GET request to a URL
response = http.request('GET', 'https://www.example.com')

# Access the data in the response
data = response.data

# Close the response to free up resources
response.close()
