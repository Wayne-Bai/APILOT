
import base64
from cryptography import x509

def deserialize_der(data):
    # Decode the DER encoded PKCS7 blob
    der = base64.b64decode(data)

    # Parse the DER encoded data as a PKCS7 object
    pkcs7 = x509.load_der_pkcs7_bytes(der, default_backend())

    # Get the certificates from the PKCS7 object
    certs = []
    for content in pkcs7.get_raw_values():
        if content["contentType"] == "certificate":
            certs.append(x509.load_der_x509_certificate(content, default_backend()))
    
    return certs
