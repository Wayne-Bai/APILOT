import http.client

# create a connection to the server
conn = http.client.HTTPConnection('www.example.com')

# send a GET request to the server
conn.request('GET', '/')

# get the response from the server
response = conn.getresponse()

# print the headers and values
for header, value in response.getheaders():
    print(header, ':', value)
