from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding

def deserialize_pkcs7(der_data):
    # Parse the PKCS7 data
    pkcs7 = serialization.load_pem_pkcs7(der_data)

    # Extract the certificates from the PKCS7 data
    certificates = []
    for content in pkcs7['certificates']:
        certificate = serialization.load_der_x509_certificate(content)
        certificates.append(certificate)

    return certificates
