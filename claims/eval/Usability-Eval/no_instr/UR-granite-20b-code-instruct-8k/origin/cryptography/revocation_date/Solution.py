from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

# Load the certificate
with open("certificate.pem", "rb") as f:
    certificate = x509.load_pem_x509_certificate(f.read(), default_backend())

# Get the revocation date
revoked_date = certificate. revoked_date

# Print the revocation date
print(revoked_date)

