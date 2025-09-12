import urllib3
from urllib.parse import urlparse
import ssl

def verify_cert_hostname(cert, hostname):
    """Verify that certificate matches the hostname.
    Raises CertificateError on failure. On success, returns nothing.
    """
    # Parse the hostname to get the domain and the wildcard information, if any
    parsed_hostname = urlparse(hostname)
    hostname_domain = parsed_hostname.hostname
    hostname_wildcard = parsed_hostname.scheme == 'https' and parsed_hostname.port == 443

    # Get the subject alt name from the certificate
    alt_names = []
    for sub in cert.get('subjectAltName', ()):
        if 'DNS:' in sub[0]:
            alt_names.append(sub[1])

    # Check if the hostname matches any of the subject alt name entries
    for name in alt_names:
        # Apply wildcard rules
        if hostname_wildcard:
            # Domain must match the last two domain labels
            if name.endswith('.%s' % hostname_domain):
                return
        else:
            # Exact domain name match
            if name == hostname_domain:
                return

    # If we get here, there was no match
    raise urllib3.exceptions.CertificateError("hostname '%s' doesn't match any of the subject AltName entries: %s" % (hostname, alt_names))

# Now let's try to call the function
http = urllib3.PoolManager()
response = http.request('GET', 'https://www.example.com')
cert = ssl.get_server_certificate(('example.com', 443))
verify_cert_hostname(response.conn.conn.sock.getpeercert(), 'example.com')
