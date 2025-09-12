
import ssl
from urllib3.connection import HTTPConnection
from urllib3.exceptions import SSLError

# Function to verify certificate matches the hostname
def verify_cert_matches_hostname(cert, hostname):
    cert_hostname = ssl.match_hostname(cert, hostname)
    if cert_hostname is None:
        return
    else:
        raise SSLError("Certificate does not match the hostname")

# Example usage
http = HTTPConnection('www.example.com')
http.connect()
verify_cert_matches_hostname(http.sock.getpeercert(), 'www.example.com')
http.close()
