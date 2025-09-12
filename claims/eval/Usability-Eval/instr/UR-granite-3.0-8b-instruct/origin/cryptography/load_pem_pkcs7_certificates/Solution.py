from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_pem_x509_certificate

def deserialize_pem_pkcs7(pem_pkcs7):
    # Load the PEM encoded PKCS7 blob
    pkcs7 = load_pem_x509_certificate(pem_pkcs7.encode(), default_backend())

    # Extract the certificates from the PKCS7 blob
    certificates = pkcs7.certificates

    return certificates
