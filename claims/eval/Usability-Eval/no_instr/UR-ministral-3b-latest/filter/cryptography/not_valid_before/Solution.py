from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from datetime import datetime
from cryptography.hazmat.primitives.asn1 import Asn1EncodingError

# Assuming you have a certificate in PEM format that you have read from a file:
with open("cert.pem", "rb") as cert_file:
    certificate_pem = cert_file.read()

# Parse the certificate
from cryptography.x509 import load_pem_x509_certificate
certificate = load_pem_x509_certificate(certificate_pem)

# Extract the validity period
valid_start = certificate.not_valid_before
valid_end = certificate.not_valid_after

try:
    # Convert to a human-readable datetime object in UTC
    datetime_start = datetime.utcfromtimestamp(valid_start.timestamp() / 1000.0)
    datetime_end = datetime.utcfromtimestamp(valid_end.timestamp() / 1000.0)
    print(f"The validity start date and time is: {datetime_start}")
    print(f"The validity end date and time is: {datetime_end}")
except Asn1EncodingError as e:
    print(f"Error reading the validity dates from the certificate: {e}")
