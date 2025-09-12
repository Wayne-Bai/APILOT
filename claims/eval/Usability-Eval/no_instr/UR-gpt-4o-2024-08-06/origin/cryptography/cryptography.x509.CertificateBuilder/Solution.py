from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa
import datetime

# Generate a new RSA key pair for the certificate
key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Define the subject and issuer name (for self-signed, these are the same)
name = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "California"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, "San Francisco"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, "My Company"),
    x509.NameAttribute(NameOID.COMMON_NAME, "mycompany.com"),
])

# Build the certificate
certificate = x509.CertificateBuilder().subject_name(
    name
).issuer_name(
    name
).public_key(
    key.public_key()
).serial_number(
    x509.random_serial_number()
).not_valid_before(
    datetime.datetime.utcnow()
).not_valid_after(
    datetime.datetime.utcnow() + datetime.timedelta(days=365)
).add_extension(
    x509.SubjectAlternativeName([x509.DNSName("mycompany.com")]),
    critical=False,
).sign(key, hashes.SHA256())

# Serialize the private key and certificate
private_key = key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.BestAvailableEncryption(b'mypassword')
)

certificate_bytes = certificate.public_bytes(serialization.Encoding.PEM)

# Output the private key and certificate
print(f"Private Key:\n{private_key.decode('utf-8')}")
print(f"Certificate:\n{certificate_bytes.decode('utf-8')}")
