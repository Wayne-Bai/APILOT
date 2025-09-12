from cryptography.hazmat.primitives import serialization
from cryptography import x509
from cryptography.hazmat.backends import default_backend

def deserialize_pem_pkcs7_to_certificates(pem_data):
    """
    Deserialize a PEM encoded PKCS7 blob to a list of certificates.
    
    Args:
    - pem_data (bytes): PEM encoded PKCS7 data.
    
    Returns:
    - List of x509.Certificate objects.
    """
    # Load the PKCS7 and convert into x509 objects
    # The serialization.load_pem_pkcs7_certificates function will take
    # care of extracting only the certificates from the PKCS7 data
    
    certificates = serialization.load_pem_pkcs7_certificates(pem_data, backend=default_backend())
    return certificates

# Example usage
pem_pkcs7_data = b"""
-----BEGIN PKCS7-----
YOUR_ENCODED_PKCS7_DATA_HERE
-----END PKCS7-----
"""

certificates = deserialize_pem_pkcs7_to_certificates(pem_pkcs7_data)

for cert in certificates:
    print(cert.subject)
