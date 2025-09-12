from cryptography import x509
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

def deserialize_pkcs7(pkcs7_blob):
    try:
        pkcs7 = x509.load_pem_pkcs7_certificates(pkcs7_blob, default_backend())
        cert_list = [cert.public_bytes(serialization.Encoding.PEM) for cert in pkcs7]
        return cert_list
    except Exception as e:
        print("Error deserializing PKCS7:", str(e))
        return None

# Example usage
pkcs7_blob = b"-----BEGIN PKCS7-----\nMIAGCSqGSIb3DQEHAqCAMIACAQAxDTALBglghkgBZQMEASow...\n-----END PKCS7-----"
cert_list = deserialize_pkcs7(pkcs7_blob)
if cert_list:
    for cert in cert_list:
        print(cert.decode())
