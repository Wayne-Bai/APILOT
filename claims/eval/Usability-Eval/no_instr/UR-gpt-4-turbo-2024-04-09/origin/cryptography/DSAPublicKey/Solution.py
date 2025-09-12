from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat

# Generate a private key for use in the key generation process
private_key = dsa.generate_private_key(key_size=2048)

# Extract the public key from the private key
public_key = private_key.public_key()

# Serialize the public key to be transferred or saved
public_key_bytes = public_key.public_bytes(
    encoding=Encoding.PEM,
    format=PublicFormat.SubjectPublicKeyInfo
)

print(public_key_bytes.decode())
