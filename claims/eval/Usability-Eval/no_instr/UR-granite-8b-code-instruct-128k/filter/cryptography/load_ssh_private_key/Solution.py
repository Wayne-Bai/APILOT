from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

def deserialize_private_key(openssh_encoded_data):
    private_key = serialization.load_pem_private_key(openssh_encoded_data)
    return private_key.private_numbers().n
