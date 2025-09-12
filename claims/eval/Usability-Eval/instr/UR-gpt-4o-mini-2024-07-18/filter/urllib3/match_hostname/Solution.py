import urllib3
from urllib3.exceptions import CertificateError
import ssl
import socket

def verify_cert_hostname(cert, hostname):
    # Extract the subject alternative names from the certificate
    if 'subjectAltName' in cert:
        san = cert['subjectAltName']
        dns_names = [entry[1] for entry in san if entry[0] == 'DNS']
    else:
        dns_names = []

    # Extract the common name from the subject
    common_name = None
    for entry in cert['subject']:
        if entry[0][0] == 'commonName':
            common_name = entry[0][1]
            break

    # Combine all valid names to check against the hostname
    valid_names = dns_names
    if common_name:
        valid_names.append(common_name)

    # Check if the hostname is valid against the certificate
    if not valid_names:
        raise CertificateError(f"No valid names found in certificate for {hostname}")

    # Check for hostname match according to RFC 2818
    hostname = hostname.lower()
    for name in valid_names:
        if socket.gethostbyname(name) == socket.gethostbyname(hostname):
            return
    
    # If no matches found, raise a CertificateError
    raise CertificateError(f"Hostname '{hostname}' does not match any valid certificate names: {', '.join(valid_names)}")
