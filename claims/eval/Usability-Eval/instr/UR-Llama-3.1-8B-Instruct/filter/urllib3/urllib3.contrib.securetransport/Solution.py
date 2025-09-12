# Import the urllib3 library
import urllib3

# Import the requests library, which relies on urllib3
import requests

# Create an SSL context object using urllib3
http = urllib3.PoolManager()

# Set the verify to False, and use the verify parameter to enable certificate verification if a path to a certificate file is provided.
# For purposes of communicating securely over the default ports for secure protocols, a system level.truststore configuration for a cacert.pem and the root.pem be used instead.
response = http.request('GET', 'http://example.com', headers={'User-Agent': 'Mozilla/5.0'}, verify=False)

# If you need to verify certificates, you would do so similar to the following.
# response = http.request('GET', 'https://example.com', headers={'User-Agent': 'Mozilla/5.0'})

print(response.status)
print(response.data)
