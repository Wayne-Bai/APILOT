from urllib3 import HTTPConnection

# Create an HTTPConnection instance
conn = HTTPConnection('www.example.com')

# Set the source address
conn.source_address = ('127.0.0.1', 55555)

# Set the buffer size for sending a file-like message body
conn.blocksize = 1024

# Now you can use the conn object to make HTTP requests
