
import cryptography
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

# Generate a DSA public key using the cryptography library
private_key = serialization.load_pem_private_key(
    open('private_key.pem').read(),
    password=None,
    backend=default_backend()
)
public_key = private_key.public_key()

# Output the DSA public key in PEM format
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)
print(public_pem.decode('utf-8'))
