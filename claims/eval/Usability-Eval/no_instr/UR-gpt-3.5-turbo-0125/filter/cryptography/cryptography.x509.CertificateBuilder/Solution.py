
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.hashes import SHA256

# Generate a private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

# Create a certificate builder
builder = x509.CertificateBuilder()

# Add a subject name
builder = builder.subject_name(x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "California"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, "Mountain View"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, "ACME Inc."),
    x509.NameAttribute(NameOID.COMMON_NAME, "www.acme.com")
]))

# Add a valid duration
valid_from = datetime.datetime.utcnow()
valid_to = valid_from + datetime.timedelta(days=365)
builder = builder.not_valid_before(valid_from)
builder = builder.not_valid_after(valid_to)

# Add the public key
public_key = private_key.public_key()
builder = builder.public_key(public_key)

# Self-sign the certificate
builder = builder.issuer_name(builder._subject)
builder = builder.sign(private_key, SHA256(), default_backend())

# Serialize the certificate to PEM format
certificate = builder.public_bytes(serialization.Encoding.PEM)

print(certificate.decode())
