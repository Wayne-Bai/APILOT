
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
from cryptography.hazmat.primitives.serialization import load_der_x509_certificate
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec

def deserialize_pkcs7_certificates(pkcs7_blob):
    certificates = []
    try:
        certificates = pkcs7_blob.get_certificates()
    except AttributeError:
        pass

    if not certificates:
        return None

    cert_list = []
    
    for cert_bytes in certificates:
        cert = load_der_x509_certificate(cert_bytes, default_backend())
        cert_list.append(cert)

    return cert_list
