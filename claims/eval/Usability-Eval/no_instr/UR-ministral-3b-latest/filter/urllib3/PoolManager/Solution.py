import urllib3

# Create a connection from the pool
http = urllib3.PoolManager()

# Define the raw URL
url = "https://example.com/endpoint"

# Extract the request-uri portion of the URL
request_uri = url.split("://")[1].split("/", 2)[0]

# Perform an HTTP request
response = http.request("GET", f"https://{request_uri}")

print(f"Status Code: {response.status}")
print(f"Response Body: {response.data}")
