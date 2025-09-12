from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_der_pkcs7_certificates
from cryptography.exceptions import InvalidSignature

def deserialize_pkcs7_der(der_blob):
    """
    Deserialize a DER encoded PKCS7 blob to a list of certificates.
    
    Args:
        der_blob (bytes): The DER encoded PKCS7 blob.
        
    Returns:
        list: A list of certificates.
    """
    try:
        certificates = load_der_pkcs7_certificates(der_blob, default_backend())
        return certificates
    except Exception as e:
        print(f"Error deserializing PKCS7: {e}")
        return []

# Example usage (you would provide your actual DER blob):
# der_blob = b'...'  # Replace with your DER encoded PKCS7 blob
# certificates = deserialize_pkcs7_der(der_blob)
# for cert in certificates:
#     print(cert)
