from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

# Generate our key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,  # The key size can be 1024, 2048, or 4096 bits
    backend=default_backend()
)

# Save the private key in a file
with open("private_key.pem", "wb") as f:
    f.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ))
