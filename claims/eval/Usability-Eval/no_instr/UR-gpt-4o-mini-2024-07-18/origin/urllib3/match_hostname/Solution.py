import urllib3
from urllib3.util.ssl_ import create_urllib3_context
import socket
import ssl

def verify_hostname(cert, hostname):
    # First, check for IP addresses
    try:
        socket.inet_pton(socket.AF_INET, hostname)
        raise ssl.CertificateError("IP addresses are not accepted for hostname.")
    except socket.error:
        pass  # It's not an IP address

    # Verify the certificate against the hostname
    subject_alt_name = cert.get('subjectAltName', [])
    common_name = None

    # Check Subject Alternative Name (SAN)
    for typ, val in subject_alt_name:
        if typ == 'DNS':
            if val.lower() == hostname.lower():
                return

    # Check Common Name (CN) if no SAN is present
    for attr in cert.get('subject', []):
        if attr[0][0] == 'commonName':
            common_name = attr[0][1]
            break

    if common_name and common_name.lower() == hostname.lower():
        return

    raise ssl.CertificateError(f"Hostname '{hostname}' does not match certificate.")

# Example usage:
# context = create_urllib3_context()
# with urllib3.PoolManager(ssl_context=context) as http:
#     cert = http.request('GET', 'https://example.com').getpeercert()
#     verify_hostname(cert, 'example.com')
