from cryptography import x509
from datetime import datetime
# Load the certificate data
with open("certificate.pem", "rb") as certificate_file:
    certificate_data = certificate_file.read()
# Parse the certificate
certificate = x509.load_pem_x509_certificate(certificate_data)
# Check if the certificate is revoked
if certificate.revoked:
    # Get the revocation date
    revocation_date = certificate.revoked.revocation_date
    # Convert the revocation date to a naive datetime
    naive_revocation_date = datetime(revocation_date.year, revocation_date.month, revocation_date.day, revocation_date.hour, revocation_date.minute, revocation_date.second)
    print("Certificate revoked on:", naive_revocation_date)
else:
    print("Certificate is not revoked.")
