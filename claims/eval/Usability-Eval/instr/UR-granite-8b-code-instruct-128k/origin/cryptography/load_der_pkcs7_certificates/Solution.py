from cryptography import serialization
from cryptography.hazmat.primitives import serialization as hazmat_serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives. padding import pad, unpad
from cryptography.hazmat.backends import default_backend

def deserialize_der_pkcs7_to_certificates(der_blob):
    pkcs7 = serialization.load_der_pkcs7_certificates(der_blob)
    certificates = []
    for cert in pkcs7:
        certificates.append(cert.public_key())
    return certificates
