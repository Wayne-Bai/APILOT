from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.pkcs7 import ContentInfo, load_pem_pkcs7_certificates

def extract_certificates(pkcs7_data):
    content_info = ContentInfo.load(pkcs7_data, default_backend())
    pkcs7 = content_info.content
    certificates = [x509.load_der_x509_certificate(certificate_data, default_backend())
                    for certificate_data in pkcs7.certificates]
    return certificates
