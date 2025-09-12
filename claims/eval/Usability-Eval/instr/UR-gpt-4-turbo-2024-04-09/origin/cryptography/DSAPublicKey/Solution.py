from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.backends import default_backend

# Generate a private DSA key
private_key = dsa.generate_private_key(
    key_size=2048,
    backend=default_backend()
)

# Obtain the public key from the private key
public_key = private_key.public_key()

# Serializing the public key to PEM format
pem_public_key = public_key.public_bytes(
    encoding=cryptography.hazmat.primitives.serialization.Encoding.PEM,
    format=cryptography.hazmat.primitives.serialization.PublicFormat.SubjectPublicKeyInfo
)

print(pem_public_key.decode())
