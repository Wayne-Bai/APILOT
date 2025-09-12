import urllib3
from urllib3.exceptions import SSLError
from urllib3.util.ssl_ import match_hostname

def verify_cert_hostname(cert, hostname):
    """
    Verify that the certificate matches the hostname.

    :param cert: Certificate in decoded format as returned by SSLSocket.getpeercert()
    :param hostname: Hostname to verify against
    :raises CertificateError: If the certificate does not match the hostname
    """
    try:
        match_hostname(cert, hostname)
    except SSLError as e:
        raise CertificateError("Certificate does not match hostname") from e

class CertificateError(ValueError):
    """Custom exception for certificate verification errors."""
    pass
