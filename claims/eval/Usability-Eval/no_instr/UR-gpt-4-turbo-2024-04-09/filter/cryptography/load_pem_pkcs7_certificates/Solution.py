from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import pkcs7

def deserialize_pem_to_certificates(pem_data):
    # Load the PEM data
    pkcs7_data = pkcs7.load_pem_pkcs7_certificates(pem_data)

    # Extract certificates only, ignore CRLs
    certificates = pkcs7_data.certificates

    return certificates

# Example usage
pem_blob = b"""
-----BEGIN PKCS7-----
... your PEM encoded PKCS7 data here ...
-----END PKCS7-----
"""
certificates = deserialize_pem_to_certificates(pem_blob)
for cert in certificates:
    print(cert)
