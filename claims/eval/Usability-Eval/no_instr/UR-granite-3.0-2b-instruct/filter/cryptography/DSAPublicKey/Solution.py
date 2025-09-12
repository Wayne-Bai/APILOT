from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa

# Generate a new DSA key pair
private_key = dsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# Get the public key from the private key
public_key = private_key.public_key()

# Print the public key
print(public_key.public_bytes(
    encoding=hashes.Hash(alg=hashes.SHA256()),
    format=hashes.PublicFormat.UncompressedPoint
))
