from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_pem_pkcs7_signed_data

def deserialize_pkcs7_pem(pem_data):
    certificates = []
    pkcs7_data = load_pem_pkcs7_signed_data(pem_data)
    
    for cert in pkcs7_data.certificates:
        certificates.append(cert)
    
    return certificates
