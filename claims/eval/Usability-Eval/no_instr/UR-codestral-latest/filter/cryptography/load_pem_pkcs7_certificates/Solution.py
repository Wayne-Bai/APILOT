from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives._asn1_pem import read_pem
from cryptography.hazmat.primitives._asn1_pkcs7 import ContentInfo, PKCS7

def pem_to_certs(pem_blob):
    pem_data, _ = read_pem(pem_blob, b"CERTIFICATE")
    content_info = ContentInfo.load(pem_data)
    pkcs7 = PKCS7.load(content_info['content'])

    certificates = []
    for content in pkcs7['contents']:
        cert = x509.load_der_x509_certificate(content['certificate']['certificate'].native, default_backend())
        certificates.append(cert)

    return certificates
