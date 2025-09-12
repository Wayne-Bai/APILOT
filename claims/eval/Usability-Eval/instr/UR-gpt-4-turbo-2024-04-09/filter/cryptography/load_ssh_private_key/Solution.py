from cryptography.hazmat.primitives.serialization import load_ssh_private_key
from cryptography.hazmat.backends import default_backend

def deserialize_ssh_private_key(encoded_key, password=None):
    """
    Deserialize an SSH private key into a key instance.

    Args:
    encoded_key (bytes): The OpenSSH encoded private key.
    password (bytes, optional): The password for the encrypted key, if any.

    Returns:
    Private key instance.
    """
    private_key = load_ssh_private_key(
        encoded_key,
        password=password,
        backend=default_backend()
    )
    return private_key

# Example usage
# Load your SSH private key as bytes. For example:
# with open("path_to_your_private_key", "rb") as key_file:
#     private_key_data = key_file.read()
#
# Call the function with the key data. If your key is encrypted, provide the password.
# my_private_key = deserialize_ssh_private_key(private_key_data, b'your_key_password')
