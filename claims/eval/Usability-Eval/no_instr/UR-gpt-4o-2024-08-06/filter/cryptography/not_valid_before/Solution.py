from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from datetime import datetime, timedelta
import pytz

# Generate a private key for use in the certificate
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# Builder for the X.509 certificate
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"US"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"California"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, u"San Francisco"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"My Company"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"mywebsite.com"),
])

# Create the validity period for the certificate
valid_from = datetime.utcnow().replace(tzinfo=pytz.UTC)  # Naive datetime representing the start
valid_until = valid_from + timedelta(days=365)  # Certificate valid for one year

# Build the certificate
certificate = x509.CertificateBuilder().subject_name(
    subject
).issuer_name(
    issuer
).public_key(
    private_key.public_key()
).serial_number(
    x509.random_serial_number()
).not_valid_before(
    valid_from
).not_valid_after(
    valid_until
).add_extension(
    x509.SubjectAlternativeName([x509.DNSName(u"mywebsite.com")]),
    critical=False,
).sign(private_key, hashes.SHA256())

# Serialize the certificate to PEM format
pem_certificate = certificate.public_bytes(encoding=serialization.Encoding.PEM)

# Output the certificate
print(pem_certificate.decode("utf-8"))
