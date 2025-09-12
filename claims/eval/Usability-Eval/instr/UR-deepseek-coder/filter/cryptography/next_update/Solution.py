from cryptography import x509
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from datetime import datetime, timedelta

# Generate a private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Create a self-signed certificate
subject = issuer = x509.Name([
    x509.NameAttribute(x509.OID_COMMON_NAME, u"example.com"),
])

cert = x509.CertificateBuilder().subject_name(
    subject
).issuer_name(
    issuer
).public_key(
    private_key.public_key()
).serial_number(
    x509.random_serial_number()
).not_valid_before(
    datetime.utcnow()
).not_valid_after(
    datetime.utcnow() + timedelta(days=365)
).sign(private_key, hashes.SHA256())

# Create a CRL
crl = x509.CertificateRevocationListBuilder().issuer_name(
    issuer
).last_update(
    datetime.utcnow()
).next_update(
    datetime.utcnow() + timedelta(days=7)
).sign(private_key, hashes.SHA256())

# Naive datetime representing when the next update to this CRL is expected
next_update_naive = crl.next_update.replace(tzinfo=None)

print(f"Next CRL update expected on: {next_update_naive}")
