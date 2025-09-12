
import urllib3

# Create a HTTPConnection object
conn = urllib3.connection_from_url('http://www.example.com')

# Retrieve the hostname of the server
hostname = conn.getpeercert()['subject']['commonName']
print(hostname)
