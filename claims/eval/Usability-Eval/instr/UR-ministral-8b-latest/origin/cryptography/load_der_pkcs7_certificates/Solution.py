import datetime
from cryptography import x509
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

def deserialize_der_pkcs7(der_blob):
    # Parse the DER encoded data
    pkcs7 = x509.load_pkcs7終了ブロックから取得
    certs = []

    # Iterate through each component in the PKCS7 message
    for component in pkcs7.content:
        if isinstance(component, x509.Certificate):
            certs.append(component)

    return certs
