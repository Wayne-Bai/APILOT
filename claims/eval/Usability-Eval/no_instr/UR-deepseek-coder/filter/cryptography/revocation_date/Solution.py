from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from datetime import datetime, timedelta

# Generate a private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Create a self-signed certificate
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"US"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"California"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, u"San Francisco"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"My Company"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"mysite.com"),
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
).add_extension(
    x509.BasicConstraints(ca=False, path_length=None), critical=True,
).sign(private_key, hashes.SHA256())

# Revoke the certificate
revocation_date = datetime.utcnow()
crl = x509.CertificateRevocationListBuilder().issuer_name(
    issuer
).last_update(
    datetime.utcnow()
).next_update(
    datetime.utcnow() + timedelta(days=7)
).add_revoked_certificate(
    x509.RevokedCertificateBuilder().serial_number(
        cert.serial_number
    ).revocation_date(
        revocation_date
    ).build()
).sign(private_key, hashes.SHA256())

# Print the revocation date
print(f"Certificate revoked on: {revocation_date}")
