import base64
from cryptography import x509
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

def extract_certificates(pkcs7_der):
    """Deserialize a DER encoded PKCS7 blob to a list of certificates"""

    # Load the DER encoded PKCS7 data
    p7 = x509.load_der_x509_certificate(pkcs7_der, default_backend())

    # Convert the certificate to a PEM format
    cert = p7.public_key().public_bytes(
        serialization.Encoding.PEM,
        serialization.PublicFormat.SubjectPublicKeyInfo
    )

    # Return the certificate as a list
    return [cert]

# Test the function
pkcs7_der = base64.b64decode("MIIClT...DVQQH...EjMCEC...iMQA==")
extracted_certificates = extract_certificates(pkcs7_der)
print(extracted_certificates)
