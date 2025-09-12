from cryptography import hsm
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from datetime import datetime, timedelta

# Generate a new RSA key pair
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Extract the public key
public_key = private_key.public_key()

# Create a new HSM
hsm_context = hsm.HSMContext(
    storage_backend="SIM",
    provider="OpenSC",
    device="SIM01",
    password="secret",
)

# Generate a new certificate
certificate = hsm_context.generate_certificate(
    subject_name=private_key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    ),
    not_valid_before=datetime.utcnow() - timedelta(days=365),
    not_valid_after=datetime.utcnow() + timedelta(days=365),
    subject=private_key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    ),
)

# Print the certificate
print(certificate)
