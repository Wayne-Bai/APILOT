import urllib3

http = urllib3.PoolManager()

# Create a request with NTLM authentication
request = urllib3.Request('http://example.com', headers={'Authorization': 'NTLM'})

# Send the request and get the response
response = http.request(request)

# Print the response
print(response.data)
