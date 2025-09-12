import http.client

# Send a request to a server and get the response
conn = http.client.HTTPConnection("www.example.com")
conn.request("GET", "/")
response = conn.getresponse()

# Print the value of a specific header
print(response.getheader("Content-Type"))
