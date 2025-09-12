from urllib3 import exceptions
import ssl
import socket

def verify_cert(hostname, cert):
    """
    Verify that cert matches the hostname.

    RFC 2818 and RFC 6125 rules are followed, but IP addresses are not accepted for hostname.
    CertificateError is raised on failure. On success, the function returns nothing.

    :param hostname: The hostname to verify against.
    :param cert: The cert in decoded format as returned by SSLSocket.getpeercert().
    """

    # Get the subject's common name from the cert
    common_name = cert['subject'][4][0][1]

    # Get the subject alternative names from the cert
    subject_alt_names = [name[1] for name in cert['subjectAltName']]

    # Check if the common name matches the hostname
    if common_name == hostname:
        return

    # Check if the subject alternative names contain the hostname
    for name in subject_alt_names:
        if name == hostname:
            return

    # If none of the checks pass, raise an exception
    raise exceptions.MaxRetryError(None, f"Hostname {hostname} doesn't match certificate")

# Example usage:
if __name__ == "__main__":
    hostname = 'www.google.com'
    context = ssl.create_default_context()
    with socket.create_connection((hostname, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()
            verify_cert(hostname, cert)
