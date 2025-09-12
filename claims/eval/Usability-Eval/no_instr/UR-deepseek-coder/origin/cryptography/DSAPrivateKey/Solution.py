from cryptography.hazmat.primitives.asymmetric.dsa import DSAPrivateKey, generate_private_key
from cryptography.hazmat.primitives import serialization

# Generate a DSA private key
private_key: DSAPrivateKey = generate_private_key(key_size=2048)

# Serialize the private key to PEM format
private_key_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

# Print the private key in PEM format
print(private_key_pem.decode())
