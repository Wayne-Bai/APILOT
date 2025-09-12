from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

def deserialize_private_key_from_openssh(private_key_data):
    private_key = serialization.load_ssh_private_key(private_key_data)
    return private_key.private_key(rsa.RSAPrivateKey)
