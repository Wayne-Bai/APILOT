from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import Encoding, PrivateFormat, NoEncryption
from cryptography.x509 import CertificateBuilder

# Generate a private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

# Define the certificate builder
builder = CertificateBuilder().subject_name(
    dn=X509Name([
        X509Name.DNSName("example.com"),
    ])
).issuer_name(
    dn=X509Name([
        X509Name.DNSName("example.com"),
    ])
).public_key(
    private_key.public_key()
).serial_number(
    X509SerialNumber(1)
).not_valid_before(
    X509Time(seconds=time.time())
).not_valid_after(
    X509Time(seconds=time.time() + 3600)
).add_extension(
    X509Extension(
        ExtensionType.KEY_USAGE, critical=True, key_usage=X509KeyUsage.DIGITAL_SIGNATURE | X509KeyUsage.KEY_ENCRYPTION
    ),
).add_extension(
    X509Extension(
        ExtensionType.BASIC_CONSTRAINTS, critical=True, basic_constraints=X509BasicConstraints.CA | X509BasicConstraints.KEY_CERT_SIGN
    ),
).sign(
    private_key, hashes.SHA256()
)

# Serialize the certificate
certificate = builder.sign(private_key, hashes.SHA256())

# Save the certificate to a file
with open("certificate.pem", "wb") as f:
    f.write(certificate.public_bytes(Encoding.PEM))
