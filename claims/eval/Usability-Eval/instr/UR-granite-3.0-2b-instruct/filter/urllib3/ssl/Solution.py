import urllib3

# Create a secure HTTP connection
http = urllib3.PoolManager(default_timeout=10)

# Create a request
request = urllib3.Request('https://www.example.com')

# Set the request method and headers
request.method = 'GET'
request.headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Send the request
response = http.request(request)

# Print the response status code
print(response.status)

# Get the response body
data = response.data
print(data)
