from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_der_x509_certificate
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography import utils
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.pki import pkcs7
import os

def deserialize_pkcs7_certificates(der_encoded_pkcs7):
    certificates = []
    
    # Load the PKCS7 object
    pkcs7_data = pkcs7.load(der_encoded_pkcs7)

    # Iterate through the PKCS7 content
    for content in pkcs7_data:
        if isinstance(content, pkcs7.Certificate):
            cert_der = content.dump()
            cert = load_der_x509_certificate(cert_der, default_backend())
            certificates.append(cert)
    
    return certificates
