from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_pem_x509_certificate

def deserialize_pkcs7_blob(pkcs7_blob):
    certificates = []
    for content in pkcs7_blob.content:
        if content.obj_type == b"CERTIFICATE":
            certificates.append(load_pem_x509_certificate(content.content, default_backend()))
    return certificates
