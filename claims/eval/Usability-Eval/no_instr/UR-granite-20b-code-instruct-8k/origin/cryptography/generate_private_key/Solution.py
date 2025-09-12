from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

# Generate a new RSA private key
private_key = rsa.generate_private_key(
 public_exponent=65537,
 key_size=2048,
 backend=default_backend()
)

# Serialize the private key to PEM format
pem = private_key.private_bytes(
 encoding=serialization.Encoding.PEM,
 format=serialization.PrivateFormat.TraditionalOpenSSL,
 encryption_algorithm=serialization.NoEncryption()
)

# Print the private key in PEM format
print(pem.decode('utf-8'))
