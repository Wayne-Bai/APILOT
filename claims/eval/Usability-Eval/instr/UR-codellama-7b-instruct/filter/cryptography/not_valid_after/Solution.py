import datetime
from cryptography.hazmat.primitives import hashes
from cryptography.x509 import Certificate

# Load the certificate from a file
with open("cert.pem", "rb") as f:
    cert = x509.load_pem_x509_certificate(f.read(), default_backend())

# Get the validity period of the certificate
validity = cert.not_valid_after - cert.not_before

# Convert the validity period to a naïve datetime representing the end of the validity period in UTC
dt = datetime.datetime(1970, 1, 1) + validity
