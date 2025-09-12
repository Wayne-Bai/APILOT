import urllib3
from urllib3.exceptions import SSLError
from urllib3.util.ssl_ import match_hostname

def verify_cert_hostname(cert, hostname):
    """
    Verify that the certificate (in decoded format) matches the hostname.
    RFC 2818 and RFC 6125 rules are followed, but IP addresses are not accepted for hostname.
    CertificateError is raised on failure. On success, the function returns nothing.
    """
    if urllib3.util.is_ip_address(hostname):
        raise ValueError("IP addresses are not accepted for hostname")
    
    try:
        match_hostname(cert, hostname)
    except SSLError as e:
        raise SSLError(f"Certificate verification failed: {e}")

# Example usage:
# cert = {'subject': ((('commonName', 'example.com'),),)}
# hostname = 'example.com'
# verify_cert_hostname(cert, hostname)
