from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.backends import default_backend

# Generate a DSA private key
private_key = dsa.generate_private_key(
    key_size=2048,  # Key size can be 1024, 2048, or 3072 (2048 or higher is recommended for adequate security)
    backend=default_backend()
)

# Example: Print the private key in PEM format
private_pem = private_key.private_bytes(
    encoding=cryptography.hazmat.primitives.serialization.Encoding.PEM,
    format=cryptography.hazmat.primitives.serialization.PrivateFormat.PKCS8,
    encryption_algorithm=cryptography.hazmat.primitives.serialization.NoEncryption()
)

print(private_pem.decode())
