from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import serialization

# Generate a DSA private key
private_key = dsa.generate_private_key(key_size=2048, backend=default_backend())

# Get the corresponding public key
public_key = private_key.public_key()

# Serialize the public key to bytes
public_key_bytes = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Output the public key
print(public_key_bytes.decode('utf-8'))
