import cryptography
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import pkcs7

def deserialize_pkcs7_to_certificates(pkcs7_blob):
    pkcs7_object = pkcs7.Pkcs7SignedData.load_der_pkcs7_certificates(pkcs7_blob, default_backend())
    certificates = [serialization.load_der_x509_certificate(cert_data, default_backend()) for cert_data in pkcs7_object.certificates]
    return certificates
