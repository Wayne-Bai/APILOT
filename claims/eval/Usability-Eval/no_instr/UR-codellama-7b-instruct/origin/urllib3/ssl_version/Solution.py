
import urllib3

# Create a client object
client = urllib3.Client(server_params={'ssl_version': 'TLSv1.2'})

# Make a request to the server
response = client.request('GET', 'https://www.example.com')

print(response.data)
