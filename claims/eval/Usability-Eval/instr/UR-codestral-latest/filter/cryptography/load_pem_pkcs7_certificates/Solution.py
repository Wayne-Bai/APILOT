from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import pkcs7

def deserialize_pkcs7(pem_data):
    pkcs7_obj = pkcs7.load_pem_pkcs7_certificates(pem_data, default_backend())
    return pkcs7_obj

# Assume pem_data is the PEM encoded PKCS7 blob
pem_data = """-----BEGIN PKCS7-----
BASE64 ENCODED DATA HERE
-----END PKCS7-----"""

certificates = deserialize_pkcs7(pem_data)
print(certificates)
