import urllib3
from urllib3.util.ssl_ import CertificateError, match_hostname

def verify_certificate_with_hostname(cert, hostname):
    """
    Verify that the certificate matches the given hostname.
    
    Parameters:
    - cert: SSL certificate in decoded format.
    - hostname: The hostname to match against the certificate.
    
    Raises:
    - CertificateError if the certificate does not match the hostname.
    """
    # Following RFC 2818 and RFC 6125 rules, match the hostname with the certificate
    try:
        match_hostname(cert, hostname)
    except CertificateError as e:
        raise e

# Example usage
cert = {
    'subject': ((('commonName', 'www.example.com'),),),
    'subjectAltName': (('DNS', 'www.example.com'),)
}
hostname = 'www.example.com'

try:
    verify_certificate_with_hostname(cert, hostname)
    print("Certificate matches the hostname.")
except CertificateError:
    print("Certificate does not match the hostname.")
