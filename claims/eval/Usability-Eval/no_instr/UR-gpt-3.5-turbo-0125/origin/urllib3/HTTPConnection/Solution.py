
import urllib3

# Create an HTTPConnection instance
conn = urllib3.connection_from_url('http://www.example.com')

# Perform operations on the HTTPConnection instance
# For example, sending an HTTP request
r = conn.request('GET', '/')
print(r.data)

# Close the connection when done
conn.close()
