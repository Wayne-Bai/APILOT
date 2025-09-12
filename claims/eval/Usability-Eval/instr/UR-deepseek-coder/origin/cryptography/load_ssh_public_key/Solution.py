from cryptography.hazmat.primitives.serialization import load_ssh_public_key
from cryptography.hazmat.backends import default_backend

def deserialize_public_key(ssh_public_key_data):
    try:
        public_key = load_ssh_public_key(ssh_public_key_data, backend=default_backend())
        return public_key
    except Exception as e:
        raise ValueError(f"Failed to deserialize public key: {e}")

# Example usage:
# ssh_public_key_data = b"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC..."
# public_key = deserialize_public_key(ssh_public_key_data)
# print(public_key)
