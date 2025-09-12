import ssl
import socket
from urllib.parse import urlparse

def verify_cert_matches_hostname(cert, hostname):
    try:
        commonName = next(v for (k, v) in cert['subject'] if k == 'commonName')
    except StopIteration:
        raise ValueError("No commonName in certificate.")

    if commonName != hostname:
        raise ssl.CertificateError("Certificate's commonName does not match hostname.")

    try:
        dnsNames = cert['subjectAltName'].get('DNS', [])
        if not any(dnsName in hostname for dnsName in dnsNames):
            raise ssl.CertificateError("Certificate's subjectAltName does not include hostname.")
    except AttributeError:
        pass

url = "https://example.com"
parsed_url = urlparse(url)

host = parsed_url.hostname
context = ssl.create_default_context()

with socket.create_connection((host, 443)) as sock:
    with context.wrap_socket(sock, server_hostname=host) as ssock:
        cert = ssock.getpeercert()

verify_cert_matches_hostname(cert, host)
