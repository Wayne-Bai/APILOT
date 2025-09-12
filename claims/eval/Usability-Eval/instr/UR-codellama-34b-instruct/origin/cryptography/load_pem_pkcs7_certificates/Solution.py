
import base64
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509 import load_pem_pkcs7_certificates

def deserialize_pkcs7(pkcs7_blob):
    # Convert the PKCS7 blob to a byte array
    pkcs7_bytes = base64.b64decode(pkcs7_blob)
    
    # Load the PKCS7 certificates
    certs = load_pem_pkcs7_certificates(pkcs7_bytes, rsa.RSAPublicKey)
    
    # Return a list of certificate objects
    return [c for c in certs]
