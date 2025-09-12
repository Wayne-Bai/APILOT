from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import binascii

def deserialize_pkcs7(der_encoded_blob):
    # Load the DER encoded PKCS7 blob
    pkcs7 = serialization.load_pem(der_encoded_blob, default_backend())

    # Check if the PKES7 contains a certificate
    if not pkcs7.is_pkcs7():
        raise ValueError("The PKES7 does not contain a certificate")

    # Extract the certificates from the PKES7
    certificates = []
    for part in pkcs7.get_parts():
        if part.tag_id == 1:
            # This is a certificate
            certificate = part.get_data()
            # Parse the certificate
            cert = x509.load_pem(certificate, default_backend())
            # Add the certificate to the list
            certificates.append(cert)

    return certificates
