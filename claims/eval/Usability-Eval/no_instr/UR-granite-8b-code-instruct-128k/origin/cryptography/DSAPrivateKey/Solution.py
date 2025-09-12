from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.backends import default_backend
# Generate a DSA private key
private_key = dsa.generate_private_key(
    key_size=2048,
    generator=2,
    backend=default_backend()
)
# Serialize the private key to a PEM-encoded string
private_key_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)
# Print the PEM-encoded string
print(private_key_pem.decode('utf-8'))
