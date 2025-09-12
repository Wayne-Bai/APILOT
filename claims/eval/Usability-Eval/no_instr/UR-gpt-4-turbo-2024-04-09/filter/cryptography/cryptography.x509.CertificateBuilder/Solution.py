from cryptography import x509
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import Encoding, PrivateFormat, NoEncryption
from cryptography.x509.oid import NameOID
from datetime import datetime, timedelta

# Generate a private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Various details about who we are
name = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "California"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, "San Francisco"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, "My Company"),
    x509.NameAttribute(NameOID.COMMON_NAME, "mycompany.com"),
])

# Validity period
valid_from = datetime.utcnow()
valid_to = valid_from + timedelta(days=365)

# Build Certificate
certificate_builder = x509.CertificateBuilder()
certificate_builder = certificate_builder.subject_name(name)
certificate_builder = certificate_builder.issuer_name(name)  # self-signed
certificate_builder = certificate_builder.public_key(private_key.public_key())
certificate_builder = certificate_builder.serial_number(x509.random_serial_number())
certificate_builder = certificate_builder.not_valid_before(valid_from)
certificate_builder = certificate_builder.not_valid_after(valid_to)
certificate_builder = certificate_builder.add_extension(
    x509.SubjectAlternativeName([x509.DNSName("mycompany.com")]),
    critical=False,
)

# Sign the certificate
certificate = certificate_builder.sign(
    private_key=private_key,
    algorithm=hashes.SHA256(),
)

# Serialize certificate
cert_pem = certificate.public_bytes(encoding=Encoding.PEM)

# Optionally serialize private key to PEM format
private_key_pem = private_key.private_bytes(
    encoding=Encoding.PEM,
    format=PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=NoEncryption()
)

print(cert_pem.decode())
print(private_key_pem.decode())
