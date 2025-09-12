
# Importing urllib3
import urllib3

# Creating a PoolManager instance
http = urllib3.PoolManager()

# Defining the method and url
method = 'GET'  # specify desired method here
url = 'http://www.example.com'  # specify absolute path here

# Sending a request to the server
response = http.request(method, url)

# Printing the response status code
print(response.status)
