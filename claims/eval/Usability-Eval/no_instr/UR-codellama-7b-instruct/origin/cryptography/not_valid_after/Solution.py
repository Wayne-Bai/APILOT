
import cryptography
from cryptography.x509 import Certificate, load_pem_x509_certificate

# Load the PEM encoded certificate
with open("certificate.pem", "rb") as f:
    cert = load_pem_x509_certificate(f.read())

# Get the NotAfter date from the certificate
not_after = cert.not_valid_after

# Convert the NotAfter date to UTC and get the end of the validity period
end_of_validity = not_after.replace(tzinfo=cryptography.x509.UTC)
