from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import pkcs7
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import base64

def deserialize_pkcs7_certificates(pem_data):
    """
    Deserialize a PEM encoded PKCS7 blob to a list of certificates.
    
    Args:
        pem_data (str): PEM encoded PKCS7 blob as a string.

    Returns:
        list: A list of loaded certificates.
    """
    # Decode the PEM data
    if pem_data.startswith("-----BEGIN PKCS7-----"):
        pem_data = pem_data.replace("-----BEGIN PKCS7-----", "").replace("-----END PKCS7-----", "")
        pkcs7_data = base64.b64decode(pem_data)
    else:
        raise ValueError("Input data does not appear to be valid PKCS7 format.")

    # Load the PKCS7 data
    pkcs7_certificates = pkcs7.load_pkcs7(pkcs7_data)

    # Extract and return only the certificates
    certs = []
    for cert in pkcs7_certificates.certificates:
        certs.append(cert)

    return certs
