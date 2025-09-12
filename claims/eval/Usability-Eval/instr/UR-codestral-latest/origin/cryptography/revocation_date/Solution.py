from cryptography import x509
from cryptography.hazmat.backends import default_backend

# dummy certificate data
certificate_data = b"..."  # replace with your certificate data

certificate = x509.load_pem_x509_certificate(certificate_data, default_backend())

revocation_date = certificate.revocation_date
print("Certificate Revocation Date: ", revocation_date)
