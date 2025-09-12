
import urllib3

# create an HTTPConnection instance with host and optional port
conn = urllib3.HTTPConnection("www.example.com", port=8080, timeout=10, source_address=("localhost", 1234), blocksize=8192)

# perform operations using the created HTTPConnection instance
# Example: conn.request('GET', '/index.html')
# Example: response = conn.getresponse()
