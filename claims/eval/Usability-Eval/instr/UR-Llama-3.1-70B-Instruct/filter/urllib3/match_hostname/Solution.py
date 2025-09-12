import urllib3
import ssl
import socket

def verify_match_hostname(cert, hostname):
    """
    Verify that the cert matches the hostname.

    Args:
    - cert (dict): The certificate in decoded format as returned by SSLSocket.getpeercert()
    - hostname (str): The hostname to verify against

    Raises:
    - ssl.CertificateError: If the cert does not match the hostname

    Returns:
    - None
    """
    try:
        # Create a match object for the hostname
        match_obj = urllib3.util.ssl_.match_hostname(cert, hostname)
        
        # If the match object is not None, it means the hostname matches the cert
        if match_obj is None:
            # If the hostname is an IP address, raise an error
            if ssl.match_hostname(cert, hostname):
                raise ssl.CertificateError("IP addresses are not accepted for hostname")
            else:
                raise ssl.CertificateError("Hostname does not match")

    except ssl.CertificateError as e:
        # If a CertificateError is raised, re-raise it
        raise ssl.CertificateError("Certificate verification failed: " + str(e))

# Example usage
if __name__ == "__main__":
    hostname = 'www.example.com'
    port = 443

    # Connect to the host using a socket
    sock = socket.create_connection((hostname, port))

    # Wrap the socket in an SSL context
    context = ssl.create_default_context()
    ssl_sock = context.wrap_socket(sock, server_hostname=hostname)

    # Get the peer's certificate
    cert = ssl_sock.getpeercert()

    try:
        # Verify the cert against the hostname
        verify_match_hostname(cert, hostname)
        print("Certificate verification succeeded")
    except ssl.CertificateError as e:
        print("Certificate verification failed: " + str(e))
    finally:
        # Close the SSL connection
        ssl_sock.close()
