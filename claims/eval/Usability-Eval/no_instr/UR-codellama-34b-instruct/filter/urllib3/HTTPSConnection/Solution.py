
import urllib3

# Create an SSL context for the connection
context = ssl.create_default_context()

# Set the protocol version and ciphers
context.options |= ssl.PROTOCOL_TLSv1_2
context.set_ciphers("ECDHE-RSA-AES256-GCM-SHA384")

# Create a secure connection using urllib3
connection = urllib3.HTTPSConnection("www.example.com", 443, context=context)

# Make a request to the server
response = connection.request("GET", "/")

# Print the response
print(response.data.decode())
