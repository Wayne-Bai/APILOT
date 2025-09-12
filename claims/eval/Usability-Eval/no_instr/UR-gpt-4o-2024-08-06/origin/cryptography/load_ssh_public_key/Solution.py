from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

def deserialize_openssh_pub_key(ssh_pub_key_data):
    """
    Deserialize a public key from OpenSSH encoded data to an instance of the public key type.
    
    :param ssh_pub_key_data: The OpenSSH encoded public key data as bytes.
    :return: A public key object.
    """
    public_key = serialization.load_ssh_public_key(
        ssh_pub_key_data,
        backend=default_backend()
    )
    return public_key

# Example usage
ssh_pub_key = b"ssh-rsa AAAAB3...examplekey... user@hostname"
public_key = deserialize_openssh_pub_key(ssh_pub_key)
print(public_key)
