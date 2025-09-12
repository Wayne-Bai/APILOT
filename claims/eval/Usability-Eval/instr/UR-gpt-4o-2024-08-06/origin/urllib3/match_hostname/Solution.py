import urllib3
from urllib3.exceptions import SSLError
from urllib3.util.ssl_ import match_hostname, CertificateError

def verify_certificate_hostname(cert, hostname):
    """
    Verifies that the certificate's common name or subject alternative name matches the given hostname.

    Args:
        cert (dict): The certificate in decoded format as returned by SSLSocket.getpeercert().
        hostname (str): The hostname to match against the certificate.

    Raises:
        CertificateError: If the certificate does not match the hostname.
    """
    if not cert:
        raise ValueError("Empty certificate provided for hostname verification.")
    
    # Check that the hostname is not an IP address
    try:
        # Attempt to parse the hostname as an IP address
        urllib3.util.connection.IS_IP(hostname)
        raise ValueError("IP address given for hostname verification; expected a valid hostname.")
    except ValueError:
        # If ValueError is raised, it means it's not a valid IP address, which is desired in this case
        pass

    try:
        # Use the urllib3 match_hostname function to verify the hostname
        match_hostname(cert, hostname)
    except CertificateError as e:
        raise CertificateError(f"Certificate did not match the expected hostname: {hostname}")

# Example usage
# cert = some_loaded_certificate  # This should be the result of an SSLSocket.getpeercert()
# verify_certificate_hostname(cert, "example.com")
