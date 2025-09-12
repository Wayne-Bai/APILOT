from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import dsa

# Generate a new DSA key pair
key = dsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Get the public key from the private key
public_key = key.public_key()

# Serialize the public key to a PEM-encoded format
public_key_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo,
)

# Print the PEM-encoded public key
print(public_key_pem.decode("utf-8"))
