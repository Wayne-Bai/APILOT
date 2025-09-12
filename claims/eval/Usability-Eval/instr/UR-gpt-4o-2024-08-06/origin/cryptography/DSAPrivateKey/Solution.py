from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import serialization

# Generate a DSA private key
private_key = dsa.generate_private_key(key_size=2048)

# To serialize the private key, we can encode it to the PEM format
pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)

# Print the private key in PEM format
print(pem.decode('utf-8'))
