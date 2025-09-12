from cryptography import x509
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

def deserialize_pkcs7(pem_data):
    # Parse the PEM encoded PKCS7 blob
    pkcs7_blob = serialization.load_pem(pem_data)

    # Check if the PKCS7 blob contains certificates
    if not isinstance(pkcs7_blob, x509.Certificate):
        raise ValueError("PKCS7 blob does not contain certificates")

    # Extract the certificates from the PKCS7 blob
    certificates = []
    for seq in pkcs7_blob.get_sequences():
        if seq.tag_id == x509.Tag.cert:
            certificates.append(seq.get_item())

    return certificates
