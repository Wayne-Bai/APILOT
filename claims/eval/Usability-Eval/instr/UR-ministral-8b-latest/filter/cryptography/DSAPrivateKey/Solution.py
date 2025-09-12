from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import serialization

# Generate a new DSA private key
private_key = dsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# Serialize the private key using DER format
pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

print(pem)
