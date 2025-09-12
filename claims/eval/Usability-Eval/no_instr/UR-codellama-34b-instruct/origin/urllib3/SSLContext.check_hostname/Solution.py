
import urllib3

# Set up SSL context
context = urllib3.TLSContext(verify_mode=urllib3.CERT_OPTIONAL)

# Wrap socket with hostname checking enabled
sock = urllib3.SSLSocket(server_hostname='www.example.com', ssl_context=context)

# Connect to server
sock.connect(('www.example.com', 443))

# Perform SSL/TLS handshake with hostname checking enabled
sock.do_handshake()

# Check if peer cert's hostname matches
if sock.getpeercert()['subjectAltName'][0].value != 'www.example.com':
    print("Peer cert's hostname does not match!")
else:
    print("Peer cert's hostname matches.")
