from cryptography import x509
from cryptography.x509.base import CertificateBuilder
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from datetime import datetime, timedelta

# Generate a private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Define the validity period
not_valid_before = datetime.utcnow()
not_valid_after = not_valid_before + timedelta(days=365)

# Create a CertificateBuilder instance
builder = x509.CertificateBuilder()

# Set the validity period
builder = builder.not_valid_before(not_valid_before)
builder = builder.not_valid_after(not_valid_after)

# Add other necessary fields to the builder (e.g., subject, issuer, public key)
builder = builder.subject_name(x509.Name([
    x509.NameAttribute(x509.NameOID.COMMON_NAME, u'example.com')
]))
builder = builder.issuer_name(x509.Name([
    x509.NameAttribute(x509.NameOID.COMMON_NAME, u'example.com')
]))
builder = builder.public_key(private_key.public_key())

# Sign the certificate with the private key
certificate = builder.sign(
    private_key=private_key,
    algorithm=hashes.SHA256(),
)

# Serialize the certificate to PEM format
certificate_pem = certificate.public_bytes(
    encoding=serialization.Encoding.PEM
)

print(certificate_pem.decode('utf-8'))
