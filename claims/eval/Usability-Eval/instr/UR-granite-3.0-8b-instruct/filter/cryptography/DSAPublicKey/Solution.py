from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa

# Generate a private key
private_key = dsa.generate_private_key(keysize=2048)

# Derive the public key from the private key
public_key = private_key.public_key()

# Print the public key
print(public_key.public_bytes(encoding=dsa.Encoding.X962, format=dsa.PublicFormat.Uncompressed))
