
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

# Decode the OpenSSH encoded private key data
private_key = serialization.load_pem_private_key(data, password=None, backend=default_backend())
