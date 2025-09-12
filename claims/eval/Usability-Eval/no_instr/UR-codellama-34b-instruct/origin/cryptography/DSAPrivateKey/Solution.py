from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

# Generate a 1024-bit DSA private key
private_key = serialization.generate_private_key(
    public_exponent=65537,
    key_size=1024,
    backend=default_backend()
)

# Export the private key to a PEM file
with open("private_key.pem", "wb") as f:
    f.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.BestAvailableEncryption(b"passphrase"),
    ))
