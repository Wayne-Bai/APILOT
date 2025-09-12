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
not_valid_after = not_valid_before + timedelta(days=365)  # 1 year validity

# Create a CertificateBuilder instance
builder = CertificateBuilder().subject_name(x509.Name([
    x509.NameAttribute(x509.NameOID.COMMON_NAME, u"example.com"),
])).issuer_name(x509.Name([
    x509.NameAttribute(x509.NameOID.COMMON_NAME, u"example.com"),
])).public_key(
    private_key.public_key()
).serial_number(
    x509.random_serial_number()
).not_valid_before(
    not_valid_before
).not_valid_after(
    not_valid_after
)

# Sign the certificate with the private key
certificate = builder.sign(
    private_key=private_key, algorithm=hashes.SHA256()
)

# Serialize the certificate to PEM format
certificate_pem = certificate.public_bytes(
    encoding=serialization.Encoding.PEM
)

print(certificate_pem.decode('utf-8'))
