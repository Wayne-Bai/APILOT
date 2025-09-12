import urllib3
from urllib3.connection import HTTPSConnection
from urllib3.exceptions import SSLError
from urllib3.util.ssl_ import ssl_wrap_socket, resolve_cert_reqs, resolve_ssl_version
import ssl

def verify_certificate_match(cert, hostname):
    """
    Verify that the certificate (cert) matches the hostname.
    RFC 2818 and RFC 6125 rules are followed, but IP addresses are not accepted.
    CertificateError is raised on failure; on success, the function returns nothing.
    
    Arguments:
    cert -- a dictionary representing the SSL certificate, as obtained from SSLContext.getpeercert()
    hostname -- a string representing the hostname to be matched with the certificate
    """
    
    # Validate that we are not checking against an IP address
    if urllib3.util.is_ipaddress(hostname):
        raise ValueError("IP addresses are not accepted as hostname")

    # Use the match_hostname from urllib3 utility
    urllib3.util.ssl_match_hostname(cert, hostname)

# Example usage with error handling
def check_ssl_certificate(url, port=443):
    """ 
    Connects to the specified HTTPS URL and port, retrieves the server's certificate,
    and verifies it against the provided hostname.
    """
    hostname = urllib3.util.parse_url(url).hostname
    conn = HTTPSConnection(host=hostname, port=port)
    
    # SSL parameters configuration
    context = ssl.create_default_context()
    cert_reqs = resolve_cert_reqs("REQUIRED")
    ssl_version = resolve_ssl_version(None)

    conn.sock = ssl_wrap_socket(conn.sock, keyfile=None, certfile=None,
                                cert_reqs=cert_reqs, ca_certs=None,
                                server_hostname=hostname, ssl_context=context,
                                ssl_version=ssl_version)

    try:
        conn.connect()
        cert = conn.sock.getpeercert()
        verify_certificate_match(cert, hostname)
        print("SSL certificate is valid.")
    except (CertificateError, SSLError) as e:
        print(f"SSL certificate validation error: {e}")
    finally:
        conn.close()

# Check SSL certificate for a specific URL
check_ssl_certificate("https://example.com")
