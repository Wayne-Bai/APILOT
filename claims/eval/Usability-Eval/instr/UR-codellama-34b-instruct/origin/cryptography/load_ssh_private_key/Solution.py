from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

def deserialize_private_key(data):
    # Use the default backend to deserialize the private key
    backend = default_backend()
    return serialization.load_pem_private_key(data, backend)
