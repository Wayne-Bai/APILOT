import urllib3

# Configure urllib3 to use pyOpenSSL as a TLS backend
http = urllib3.PoolManager(assert_hostname=False, cert_reqs='CERT_REQUIRED')

# Example API request
response = http.request('GET', 'https://www.example.com')

# Handle and print the response
print(response.status)
print(response.data.decode('utf-8'))
