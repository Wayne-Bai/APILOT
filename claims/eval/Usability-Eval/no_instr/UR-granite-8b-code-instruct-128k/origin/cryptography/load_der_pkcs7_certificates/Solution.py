from cryptography import x509
from cryptography.hazmat.primitives import serialization

def deserialize_pkcs7(der_blob):
    pkcs7 = serialization.load_der_certificate(der_blob)
    certificates = [cert for cert in pkcs7 if isinstance(cert, x509.Certificate)]
    return certificates
