from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

def deserialize_public_key(ssh_data):
    public_key = serialization.load_ssh_public_key(ssh_data, backend=default_backend())
    return public_key
