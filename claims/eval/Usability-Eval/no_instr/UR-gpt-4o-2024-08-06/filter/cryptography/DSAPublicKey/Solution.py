from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

# Generate a DSA private key
private_key = dsa.generate_private_key(
    key_size=2048,  # Key size could be 1024, 2048, or 3072 bits
    backend=default_backend()
)

# Obtain the DSA public key from the private key
public_key = private_key.public_key()

# Serialize the public key to the OpenSSH format for use or storing
public_bytes = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Display the public key in PEM format
print(public_bytes.decode('utf-8'))
