from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, ed25519, ec

def deserialize_public_key(data):
    key = serialization.load_ssh_public_key(data, default_backend())
    return key

# Sample usage
with open("id_rsa.pub", "rb") as key_file:
    public_key = deserialize_public_key(key_file.read())
    print(public_key)
