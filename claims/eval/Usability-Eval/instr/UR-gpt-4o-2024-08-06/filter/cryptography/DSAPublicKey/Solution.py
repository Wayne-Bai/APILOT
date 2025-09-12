from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dsa

# Generate a private DSA key
private_key = dsa.generate_private_key(
    key_size=2048,
    backend=default_backend()
)

# Generate the corresponding public key
public_key = private_key.public_key()

# You can serialize the public key for storage or transmission
from cryptography.hazmat.primitives import serialization

public_key_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Output the public key in PEM format
print(public_key_pem.decode('utf-8'))
