from cryptography import x509
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes, serialization
from datetime import datetime, timedelta
from cryptography.x509.oid import NameOID

# Generate private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Generate a self-signed certificate
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"US"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"California"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, u"San Francisco"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"My Company"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"mycompany.com"),
])

# Naïve datetime for the certificate's start of validity
naive_start_time = datetime.utcnow()

# Create certificate
certificate = (
    x509.CertificateBuilder()
    .subject_name(subject)
    .issuer_name(issuer)
    .public_key(private_key.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(naive_start_time)
    .not_valid_after(naive_start_time + timedelta(days=365))
    .add_extension(
        x509.SubjectAlternativeName([x509.DNSName(u"www.mycompany.com")]),
        critical=False,
    )
    .sign(private_key, hashes.SHA256())
)

# Save or use the certificate
pem_certificate = certificate.public_bytes(serialization.Encoding.PEM)
print(pem_certificate)
