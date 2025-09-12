from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.x509.loading import load_pem_x509_certificate

def deserialize_pkcs7(pkcs7_blob):
    certificates = []
    try:
        # Load the PKCS7 blob
        pkcs7 = load_pem_x509_certificate(pkcs7_blob, default_backend())

        # Iterate over the certificates in the PKCS7 blob
        for certificate in pkcs7.certificates:
            # Check if the certificate is a private key
            if certificate.is_private_key():
                continue

            # Add the certificate to the list
            certificates.append(certificate)

    except Exception as e:
        print(f"Error deserializing PKCS7 blob: {e}")

    return certificates
