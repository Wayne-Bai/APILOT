from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa

# Generate a new DSA private key
private_key = dsa.generate_private_key(key_size=1024, backend=default_backend())

# Extract the public key from the private key
public_key = private_key.public_key()
