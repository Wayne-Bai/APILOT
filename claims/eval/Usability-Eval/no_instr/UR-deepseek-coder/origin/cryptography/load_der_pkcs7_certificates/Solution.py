from cryptography import x509
from cryptography.hazmat.primitives.serialization import pkcs7
from cryptography.hazmat.primitives import serialization

def deserialize_pkcs7_to_certificates(der_encoded_pkcs7):
    # Load the DER encoded PKCS7 blob
    pkcs7_data = serialization.load_der_data(der_encoded_pkcs7)
    
    # Extract the certificates from the PKCS7 data
    certificates = []
    for cert in pkcs7_data.certificates:
        certificates.append(cert)
    
    return certificates
