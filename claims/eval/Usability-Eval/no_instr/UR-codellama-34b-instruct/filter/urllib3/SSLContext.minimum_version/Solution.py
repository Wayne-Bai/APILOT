
import urllib3

# Create a connection pool manager object
http = urllib3.PoolManager()

# Send a request to a server that supports TLS 1.2 or later
response = http.request('GET', 'https://www.example.com/')

# Check the minimum supported version of TLS
if response.is_tls:
    print(f"The minimum supported version of TLS is {response.tls_version}")
else:
    print("TLS is not supported by this server")
