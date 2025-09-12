import urllib3

# Create an HTTP client instance
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', 
                           ca_certs=urllib3.packages.six.MEMORYFILE, 
                           suppress_warnings=True)

# Usage example
url = 'http://example.com'
response = http.request('GET', url)

if response.status!= 200:
    print(f"Failed to retrieve: {response.status}")
else:
    print("Data retrieved successfully")
