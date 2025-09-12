from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from datetime import datetime, timedelta
import os

# Generate a private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Get the current time in UTC
valid_from = datetime.utcnow()
# Set the end of the validity period as a naïve datetime, 365 days in the future
valid_to = valid_from + timedelta(days=365)

# Create a certificate with the given validity period
certificate = (
    x509.CertificateBuilder()
   .subject_name(x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, u"example.com")]))
   .issuer_name(x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, u"example.com")]))
   .public_key(private_key.public_key())
   .serial_number(x509.random_serial_number())
   .not_valid_before(valid_from)
   .not_valid_after(valid_to)
   .sign(private_key, hashes.SHA256())
)
