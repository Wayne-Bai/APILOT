
import cryptography.hazmat.primitives.asymmetric.rsa as rsa
from cryptography.hazmat.primitives import serialization

def deserialize_pkcs7(pem):
    with open(pem, 'r') as f:
        pkcs7 = f.read()
    certificates = []
    for cert in serialization.load_der_pkcs7(pkcs7):
        if isinstance(cert, rsa.RSAPrivateKey) or isinstance(cert, rsa.RSAPublicKey):
            certificates.append(cert)
    return certificates
