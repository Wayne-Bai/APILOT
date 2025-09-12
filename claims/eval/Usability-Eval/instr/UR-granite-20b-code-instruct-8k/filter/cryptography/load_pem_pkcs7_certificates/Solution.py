
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

def deserialize_pkcs7(pkcs7_data):
    pkcs7 = serialization.load_pem_x509_collection(pkcs7_data, default_backend())
    return [cert for cert in pkcs7]
