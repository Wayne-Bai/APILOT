from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.x509 import load_der_x509_pkcs7_decoded_signature_info

def deserialize_pkcs7_certificates(pkcs7_bytes):
    # Initialize the backend
    backend = default_backend()

    # Decode the PKCS7 blobs
    decoded_signature_info = load_der_x509_pkcs7_decoded_signature_info(pkcs7_bytes)

    # Iterate through the signature objects in the decoded signature info
    certificates = []
    for signature in decoded_signature_info.signature:
        # Assume each signature object contains a certificate
        cert = signature.signature_object.cert[0]
        # Include validation steps if necessary
        certificates.append(cert)

    return certificates
