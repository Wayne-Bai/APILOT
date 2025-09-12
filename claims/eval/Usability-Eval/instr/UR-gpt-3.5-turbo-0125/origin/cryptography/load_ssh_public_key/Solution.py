
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

def deserialize_public_key_from_openssh(ssh_public_key_bytes):
    decoded_key = serialization.load_ssh_public_key(ssh_public_key_bytes, backend=default_backend())
    return decoded_key

# Example usage
ssh_public_key_bytes = b'your_ssh_public_key_bytes_here'
deserialized_key = deserialize_public_key_from_openssh(ssh_public_key_bytes)
print(deserialized_key)
