from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import serialization

# Generate a new private key
private_key = dsa.generate(2048)

# Derive the public key from the private key
public_key = private_key.public_key()

# Serialize the public key to PEM format
pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Print the public key in PEM format
print(pem.decode())
