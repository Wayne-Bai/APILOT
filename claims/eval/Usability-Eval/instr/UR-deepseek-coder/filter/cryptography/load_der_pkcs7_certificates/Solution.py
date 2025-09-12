from cryptography import x509
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

def deserialize_der_pkcs7_to_certificates(der_data):
    # Load the DER encoded PKCS7 data
    pkcs7_data = serialization.load_der_pkcs7_certificates(der_data, backend=default_backend())
    
    # Extract the certificates from the PKCS7 data
    certificates = []
    for cert in pkcs7_data:
        certificates.append(cert)
    
    return certificates
