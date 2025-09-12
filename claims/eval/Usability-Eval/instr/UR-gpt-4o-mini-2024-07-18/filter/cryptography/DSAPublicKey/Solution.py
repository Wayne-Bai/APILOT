from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import serialization

# Generate a DSA key pair
private_key = dsa.generate_private_key(key_size=2048, backend=default_backend())
public_key = private_key.public_key()

# Serialize the public key to PEM format
pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Print the PEM encoded public key
print(pem.decode('utf-8'))
