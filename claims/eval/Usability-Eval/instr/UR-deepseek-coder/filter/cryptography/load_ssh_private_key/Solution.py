from cryptography.hazmat.primitives.serialization import load_ssh_private_key
from cryptography.hazmat.primitives.asymmetric import rsa, dsa, ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

def deserialize_private_key(private_key_data, password=None):
    """
    Deserialize a private key from OpenSSH encoded data to an instance of the private key type.

    :param private_key_data: The OpenSSH encoded private key data.
    :param password: The password to decrypt the private key if it is encrypted.
    :return: An instance of the private key type.
    """
    key = load_ssh_private_key(private_key_data, password, default_backend())
    return key

# Example usage:
# private_key_data = b"-----BEGIN OPENSSH PRIVATE KEY-----\n..."
# password = b"your_password"
# key_instance = deserialize_private_key(private_key_data, password)
