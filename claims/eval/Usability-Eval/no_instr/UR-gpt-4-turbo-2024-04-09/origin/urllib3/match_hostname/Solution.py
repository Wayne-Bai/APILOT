import urllib3
from urllib3.util.ssl_ import assert_hostname_matches_cert

def verify_certificate(hostname, cert):
    try:
        # Verify that the certificate matches the hostname
        assert_hostname_matches_cert(cert, hostname)
        print("Certificate matches the hostname.")
    except urllib3.exceptions.SSLError as e:
        # Handle the error when the certificate does not match the hostname
        raise urllib3.exceptions.CertificateError(f"Certificate verification failed: {str(e)}")

# Example usage:
# You must replace 'hostname' with the actual hostname and 'cert' with the certificate dictionary
# Example certificate for demonstration (typically, you will get this from SSLSocket.getpeercert())
cert_example = {
    'subject': ((('commonName', 'example.com'),),),
    'subjectAltName': [('DNS', 'example.com'), ('DNS', 'www.example.com')]
}

hostname_example = 'example.com'

# Call the verification function
verify_certificate(hostname_example, cert_example)
