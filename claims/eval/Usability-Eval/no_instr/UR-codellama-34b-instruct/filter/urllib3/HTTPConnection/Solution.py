
import urllib3

# Instantiate an HTTPConnection object with host and port
conn = urllib3.HTTPConnection("www.example.com", 80)

# Set timeout for blocking operations
conn.timeout = 5

# Set source address for the HTTP connection
conn.source_address = ("localhost", 1234)

# Set buffer size in bytes for sending a file-like message body
conn.blocksize = 8192
