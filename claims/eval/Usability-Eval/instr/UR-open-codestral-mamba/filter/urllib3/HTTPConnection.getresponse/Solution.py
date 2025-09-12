# Necessary imports
import urllib3

# Create a PoolManager instance
http = urllib3.PoolManager()

# URL to send the GET request to
url = 'http://somwebsite.com'

# Send the GET request
response = http.request('GET', url)

# Extract the data and print
data = response.data
print(data)
