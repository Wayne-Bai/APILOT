
from cryptography.hazmat.primitives import serialization

def deserialize_public_key(data):
    public_key = serialization.load_ssh_public_key(data)
    return public_key
