from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

def deserialize_pkcs7_to_certificates(pkcs7_blob):
    """
    Deserializes a DER encoded PKCS7 blob to a list of certificates.
    """
    pkcs7 = serialization.load_der_pkcs7_certificates(pkcs7_blob, backend=default_backend())
    certificates = []
    for certificate in pkcs7:
        certificates.append(certificate.public_bytes(serialization.Encoding.PEM))

    return certificates
