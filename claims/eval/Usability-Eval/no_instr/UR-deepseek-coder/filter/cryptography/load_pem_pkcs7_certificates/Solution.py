from cryptography import x509
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

def deserialize_pkcs7_to_certificates(pem_data):
    # Load the PEM encoded PKCS7 blob
    pkcs7_data = serialization.load_pem_pkcs7_certificates(pem_data)
    
    # Extract and return the list of certificates
    certificates = [cert for cert in pkcs7_data]
    return certificates

# Example usage:
pem_encoded_pkcs7 = b"""-----BEGIN PKCS7-----
... (PEM encoded PKCS7 data) ...
-----END PKCS7-----"""

certificates = deserialize_pkcs7_to_certificates(pem_encoded_pkcs7)
for cert in certificates:
    print(cert.subject)
