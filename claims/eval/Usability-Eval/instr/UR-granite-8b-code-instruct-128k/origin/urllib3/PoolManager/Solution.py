import urllib3

# Create a PoolManager instance
http = urllib3.PoolManager()

# Make a request and get the response
response = http.request('GET', 'http://www.example.com/')

# Check if the response was successful
if response.status == 200:
    # Print the response body
    print(response.data)
