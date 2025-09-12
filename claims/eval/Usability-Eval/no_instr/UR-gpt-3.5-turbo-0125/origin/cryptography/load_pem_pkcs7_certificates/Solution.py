from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import Encoding
from cryptography.hazmat.primitives.serialization import PublicFormat
from cryptography import x509

def deserialize_pem_pkcs7_to_certificates(pem_data):
    certificates = []
    
    pkcs7_data = x509.load_pem_x509_certificate(pem_data, default_backend())
    
    if pkcs7_data.type == x509.PKCS7:
        for cert in pkcs7_data.certificates:
            certificates.append(cert.public_bytes(Encoding.PEM))
    
    return certificates
