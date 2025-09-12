from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography import x509
from cryptography.hazmat.primitives.serialization.pkcs7 import PKCS7LoadOptions

def deserialize_pkcs7_certificates(der_data):
    # Load PKCS7 data
    pkcs7_obj = serialization.load_der_pkcs7_data(
        data=der_data,
        options=PKCS7LoadOptions()
    )
    
    # Extract certificates
    certificates = []
    for cert in pkcs7_obj:
        if isinstance(cert, x509.Certificate):
            certificates.append(cert)
    
    return certificates

# Example usage
# der_data = b'...'  # DER encoded PKCS7 blob
# certificates = deserialize_pkcs7_certificates(der_data)
# for cert in certificates:
#     print(cert.subject)
