
import datetime
from cryptography import x509

# Load the TLS certificate from disk
with open("certificate.pem", "rb") as f:
    cert_der = f.read()

# Parse the DER-encoded certificate
cert = x509.load_der_x509_certificate(cert_der)

# Extract the validity period from the certificate
not_before = datetime.datetime.strptime(cert.not_valid_before, "%Y%m%d%H%M%SZ")
not_after = datetime.datetime.strptime(cert.not_valid_after, "%Y%m%d%H%M%SZ")

# Convert the validity period to UTC
utc_not_before = not_before.astimezone(datetime.timezone.utc)
utc_not_after = not_after.astimezone(datetime.timezone.utc)

print("Certificate validity period:", utc_not_before, "to", utc_not_after)
