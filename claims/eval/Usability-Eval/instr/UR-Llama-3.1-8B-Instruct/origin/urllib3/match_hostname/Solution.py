import urllib3
import ssl

def verify_certificate(hostname, port=443, timeout=5):
    """
    Verify that the server's certificate matches the hostname.

    Args:
        hostname (str): The hostname to verify.
        port (int, optional): The port to verify. Defaults to 443.
        timeout (int, optional): The timeout in seconds. Defaults to 5.

    Raises:
        CertificateError: If the certificate verification fails.
    """

    # Create an SSL context
    context = ssl.create_default_context()

    # Disable hostname verification for urllib3
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    # Create an HTTP connection
    http = urllib3.PoolManager(ca_certs_file='/etc/ssl/certs/ca-certificates.crt')

    # Try connecting to the server with the specified timeout
    try:
        response = http.request('GET', f'https://{hostname}:{port}/', timeout=timeout)
        # Get the server's certificate
        server_cert = ssl.SSLContext().wrap_socket(urllib3.connection.HTTPSConnectionPool(f'https://{hostname}:{port}').get_conn().context._ssltls_connection._getServer().server_values, server_hostname=hostname).getpeercert(binary_form=False)
        
        # Get the server's hostname from the certificate
        cert_hostname = server_cert.get('subjectAltName', [])[0][1] if'subjectAltName' in server_cert else None

        # If no subjectAltName, use the CN
        if not cert_hostname:
            cert_hostname = server_cert.get('subject', [])[0][1]

        # Verify that the certificate matches the hostname
        if cert_hostname!= hostname:
            raise CertificateError("Certificate does not match hostname")

    except urllib3.MaxRetryError as e:
        raise CertificateError("Certificate verification failed") from e
    except urllib3.timeout.TimeoutError as e:
        raise CertificateError("Certificate verification timed out") from e
    except urllib3.exceptions.NewConnectionError as e:
        raise CertificateError("Failed to establish a new connection") from e
    except ssl.SSLError as e:
        raise CertificateError("SSLError: {}".format(e))

class CertificateError(Exception):
    """Base class for exceptions in this module."""
    pass
