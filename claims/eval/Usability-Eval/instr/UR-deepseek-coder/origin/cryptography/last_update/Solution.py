from cryptography import x509
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.x509.oid import NameOID
import datetime

# Generate a private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Create a self-signed certificate
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "California"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, "San Francisco"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, "My Company"),
    x509.NameAttribute(NameOID.COMMON_NAME, "mysite.com"),
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
    datetime.datetime.utcnow()
).not_valid_after(
    datetime.datetime.utcnow() + datetime.timedelta(days=365)
).sign(private_key, hashes.SHA256())

# Create a CRL
crl = x509.CertificateRevocationListBuilder().issuer_name(
    issuer
).last_update(
    datetime.datetime.utcnow()
).next_update(
    datetime.datetime.utcnow() + datetime.timedelta(days=7)
).add_revoked_certificate(
    x509.RevokedCertificateBuilder().serial_number(
        cert.serial_number
    ).revocation_date(
        datetime.datetime.utcnow()
    ).build()
).sign(private_key, hashes.SHA256())

# Naive datetime representing when this CRL was last updated
last_update_naive = crl.last_update.replace(tzinfo=None)
print(f"Last update (naive datetime): {last_update_naive}")
