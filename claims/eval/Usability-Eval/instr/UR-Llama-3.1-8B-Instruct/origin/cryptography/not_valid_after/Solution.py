# Import necessary libraries
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography import x509
from cryptography.x509.oid import NameOID
from datetime import datetime, timedelta
import ipaddress

# Use RSA key pair for signing
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

# Extract the subject
subject = x509.Name([
    x509.NameAttribute(NameOID.COMMON_NAME, u"example.com")
])

# Set not-after date in the future
not_after = datetime.utcnow() + timedelta(days=365)  # 1 year from today

# Create the certificates
certificate = (
    x509.CertificateBuilder()
   .subject_name(subject)
   .issuer_name(subject)
   .public_key(private_key.public_key())
   .serial_number(x509.random_serial_number())
   .not_valid_before(datetime.utcnow())
   .not_valid_after(not_after)
   .build()
)

# Build the private key in PEM format.
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)

# Build the public key in PEM format.
public_pem = private_key.public_key().public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Build the certificate in PEM format
certificate_bundle = certificate.public_bytes(serialization.Encoding.PEM)

print("The private key is:")
print(private_pem.decode('utf-8'))
print("\nThe public key is:")
print(public_pem.decode('utf-8'))
print("\nThe certificate bundle is:")
print(certificate_bundle.decode('utf-8'))
