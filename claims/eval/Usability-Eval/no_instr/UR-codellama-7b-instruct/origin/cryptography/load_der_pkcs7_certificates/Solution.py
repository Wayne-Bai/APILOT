
from cryptography.x509 import _Certificate
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends.openssl.backend import backend

def decode_pkcs7(der_data):
    pkcs7 = backend.load_der_pkcs7_bytes(der_data)
    certs = []
    for blob in pkcs7.get_authenticated_attribute(0x17).get_values():
        cert = _Certificate(blob, rsa._RSAPublicKey)
        certs.append(cert)
    return certs
