from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import serialization

# Generate a new private key
private_key = dsa.generate_private_key()

# Generate a corresponding public key
public_key = private_key.public_key()

# Serializing the public key to PEM format
public_key_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

print(public_key_pem.decode('utf-8'))
