from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.x509.oid import ExtensionOID
from datetime import datetime, timedelta

# Load the certificate
with open("certificate.pem", "rb") as f:
    cert = x509.load_pem_x509_certificate(f.read(), default_backend())

# Extract the not_valid_after value from the certificate
not_valid_after = cert.not_valid_after

# Add a timedelta of 30 days to the not_valid_after value
end_of_validity = not_valid_after + timedelta(days=30)

print("End of validity: ", end_of_validity)
