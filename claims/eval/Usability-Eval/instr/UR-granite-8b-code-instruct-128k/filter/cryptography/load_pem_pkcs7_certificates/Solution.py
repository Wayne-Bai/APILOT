
from cryptography import x509
from cryptography.hazmat.backends import default_backend

def deserialize_pem_certificates(pem_data):
    pkcs7 = x509.load_pem_pkcs7_certificates(pem_data, default_backend())
    certificates = []
    for cert in pkcs7:
        if isinstance(cert, x509.Certificate):
            certificates.append(cert)

    return certificates
