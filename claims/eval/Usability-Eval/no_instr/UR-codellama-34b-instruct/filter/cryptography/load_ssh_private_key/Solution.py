
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

# Read the OpenSSH encoded private key file
with open('private_key.pem', 'rb') as f:
    private_key = serialization.load_pem_private_key(f.read(), backend=default_backend())

print("Private Key Type:", type(private_key))
