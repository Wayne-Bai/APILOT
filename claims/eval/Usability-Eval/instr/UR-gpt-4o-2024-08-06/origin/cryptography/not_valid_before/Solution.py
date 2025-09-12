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

# Create a builder for the certificate
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"US"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"California"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, u"San Francisco"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"My Company"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"mycompany.com"),
])

builder = x509.CertificateBuilder()
builder = builder.subject_name(subject)
builder = builder.issuer_name(issuer)
builder = builder.public_key(private_key.public_key())
builder = builder.serial_number(x509.random_serial_number())

# Set the validity period for the certificate
not_valid_before = datetime.datetime.utcnow()
not_valid_after = not_valid_before + datetime.timedelta(days=365)  # 1 year validity

builder = builder.not_valid_before(not_valid_before)
builder = builder.not_valid_after(not_valid_after)

builder = builder.add_extension(
    x509.SubjectAlternativeName([x509.DNSName(u"mycompany.com")]),
    critical=False,
)

# Sign the certificate with the private key
certificate = builder.sign(
    private_key=private_key, algorithm=hashes.SHA256()
)

# Serialize the certificate
cert_pem = certificate.public_bytes(encoding=serialization.Encoding.PEM)

# Print the certificate
print(cert_pem.decode('utf-8'))
