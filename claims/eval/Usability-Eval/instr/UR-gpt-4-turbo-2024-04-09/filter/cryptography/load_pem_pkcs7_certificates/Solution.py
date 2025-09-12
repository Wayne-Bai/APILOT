from cryptography.hazmat.primitives.serialization import pkcs7
from cryptography.hazmat.primitives import hashes
from cryptography import x509
from cryptography.hazmat.backends import default_backend

def deserialize_pem_pkcs7_to_certificates(pem_data):
    # Load the PEM data into a PKCS7 object
    pkcs7_object = pkcs7.load_pem_pkcs7_certificates(pem_data, backend=default_backend())

    # Extract certificates, ignoring other data types like CRLs
    certificates = [cert for cert in pkcs7_object.certificates]

    return certificates

# Example usage
pem_data = b"""
-----BEGIN PKCS7-----
MIIBaAYJKoZIhvcNAQcDoIIBZTCCAWEGCSqGSIb3DQEHATAcBgoqhkiG9w0BDAED
...
-----END PKCS7-----
"""
certificates = deserialize_pem_pkcs7_to_certificates(pem_data)
for cert in certificates:
    print(cert)
