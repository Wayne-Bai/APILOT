from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import load_pem_x509_certificate

def deserialize_pkcs7(pkcs7_blob):
    certificates = []
    for content in pkcs7_blob:
        if content[0] == b'30':  # Check if the content is a certificate
            cert = serialization.load_pem_x509_certificate(content, default_backend())
            certificates.append(cert)
    return certificates
