from datetime import datetime, timezone
from cryptography.hazmat.primitives import serialization
from cryptography.x509.extensions import AuthorityKeyIdentifier, BasicConstraints

# Create a new certificate
cert = x509.CertificateBuilder()

# Set the validity period for the certificate
not_before = datetime(2017, 1, 1, tzinfo=timezone.utc)
not_after = datetime(2018, 12, 31, tzinfo=timezone.utc)
cert.set_validity(not_before, not_after)

# Add an Authority Key Identifier extension to the certificate
aki = AuthorityKeyIdentifier()
cert.add_extension(aki, critical=False)

# Add a Basic Constraints extension to the certificate
bc = BasicConstraints()
cert.add_extension(bc, critical=True)

# Generate a self-signed certificate
pkey = rsa.generate_private_key(public_exponent=65537, key_size=2048)
certificate = cert.sign(pkey, hashes.SHA256(), default_backend())

# Print the serial number and authority key identifier of the certificate
print("Serial number:", certificate.serial_number)
print("Authority Key Identifier:", aki.value)
