import urllib3

# Create an HTTPConnection instance
conn = urllib3.HTTPConnection("example.com", timeout=5, source_address=('127.0.0.1', 8000))
