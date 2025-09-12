from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, ec
from cryptography.hazmat.backends import default_backend

def deserialize_ssh_public_key(ssh_public_key_data):
    """
    Deserialize a public key from OpenSSH encoded data to an instance of the public key type.

    :param ssh_public_key_data: The OpenSSH encoded public key data as a byte string
    :return: An instance of the public key type
    """
    public_key = serialization.load_ssh_public_key(
        ssh_public_key_data,
        backend=default_backend()
    )
    return public_key

# Example usage
ssh_key_data = b'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQD... user@hostname'
public_key = deserialize_ssh_public_key(ssh_key_data)
print(type(public_key))
