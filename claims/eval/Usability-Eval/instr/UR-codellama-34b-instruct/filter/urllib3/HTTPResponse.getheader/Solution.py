
import http.client

# create a connection object
conn = http.client.HTTPConnection("www.example.com")

# send request to server
conn.request("GET", "/")

# get the response from server
response = conn.getresponse()

# print the value of header for the response
print(response.headers)

# close the connection
conn.close()
