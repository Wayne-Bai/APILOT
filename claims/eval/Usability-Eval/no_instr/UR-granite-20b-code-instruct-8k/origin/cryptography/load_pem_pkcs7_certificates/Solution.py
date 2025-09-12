import cryptography
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_x509_csr

# deserialize a PEM encoded PKCS7 blob to a list of certificates
def deserialize_pkcs7(pkcs7_blob):
    # load the PKCS7 blob into a Python object
    pkcs7 = serialization.load_pem_pkcs7_certificate_request(pkcs7_blob, default_backend())
    
    # extract the certificates from the PKCS7 object
    certificates = []
    for cert in pkcs7.certificates:
        # load the certificate into a Python object
        certificate =serialization.load_der_x509_certificate(cert.public_bytes(serialization.Encoding.DER), default_backend())
        certificates.append(certificate)
    
    return certificates
