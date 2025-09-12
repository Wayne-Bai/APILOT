from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from datetime import datetime, timezone

# Generate a private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

# Generate a public key
public_key = private_key.public_key()

# Create a certificate builder
builder = x509.CertificateBuilder()

# Set the subject of the certificate
builder = builder.subject_name(x509.Name([
    x509.NameAttribute(x509.oid.NameOID.COMMON_NAME, u"www.example.com")
]))

# Set the public key of the certificate
builder = builder.public_key(public_key)

# Set the not before time of the certificate
not_before = datetime.utcnow().replace(tzinfo=timezone.utc)
builder = builder.not_valid_before(not_before)

# Set the not after time of the certificate
not_after = not_before + datetime.timedelta(days=365)
builder = builder.not_valid_after(not_after)

# Set the serial number of the certificate
builder = builder.serial_number(x509.random_serial_number())

# Sign the certificate with the private key
certificate = builder.sign(private_key, hashes.SHA256(), default_backend())

# Serialize the certificate to PEM format
pem_certificate = certificate.public_bytes(serialization.Encoding.PEM)

# Print the PEM certificate
print(pem_certificate.decode('utf-8'))
