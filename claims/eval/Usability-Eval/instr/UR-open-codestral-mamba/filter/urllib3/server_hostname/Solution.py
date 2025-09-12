import urllib3

# Create a urllib3 PoolManager instance
http = urllib3.PoolManager()

# Specify the server hostname
hostname = "your_hostname_here"

# If no hostname is specified, set it to None
if not hostname:
    hostname = None

# Make a request to the server
response = http.request('GET', f"http://{hostname}")

# The data sent by the server can be obtained
data = response.data
print(data)
