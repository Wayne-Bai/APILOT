import urllib3

# Define the headers you want to include in the request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
}

# Create a request object
http = urllib3.PoolManager()
req = http.request('GET', 'https://example.com', headers=headers)

# Print the headers of the response
print(req.data.decode('utf-8'))

# Close the connection
http.close()
