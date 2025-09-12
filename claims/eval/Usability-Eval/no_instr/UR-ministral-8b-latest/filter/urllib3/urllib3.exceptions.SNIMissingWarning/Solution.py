import urllib3

# Disable SNI
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Create a pool manager
http = urllib3.PoolManager()

# Define the URL
url = "https://www.example.com"

# Make the request
response = http.request('GET', url, cert_reqs='CERT_NONE')

# Output the response
print(response.data)
