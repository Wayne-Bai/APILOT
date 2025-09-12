from cryptography.hazmat.primitives.serialization import load_ssh_public_key
from cryptography.hazmat.backends import default_backend

def deserialize_public_key(openssh_data):
    try:
        public_key = load_ssh_public_key(openssh_data, backend=default_backend())
        return public_key
    except Exception as e:
        print(f"Failed to deserialize public key: {e}")
        return None

# Example usage:
# openssh_data = b"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC..."
# public_key = deserialize_public_key(openssh_data)
# if public_key:
#     print("Public key deserialized successfully.")
