from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

def deserialize_pem_pkcs7_to_certs(pem_data):
    # Load the PEM encoded PKCS7 data
    pem_bytes = pem_data.encode('utf-8')
    pkcs7_data = serialization.load_pem_pkcs7_certificates(pem_bytes)
    
    # Extract certificates from the PKCS7 data
    certificates = []
    for cert_data in pkcs7_data:
        cert = x509.load_der_x509_certificate(cert_data, default_backend())
        certificates.append(cert)
    
    return certificates
