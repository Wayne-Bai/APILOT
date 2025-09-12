from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

def load_ssh_public_key(ssh_public_key_data: bytes):
    """
    Deserialize a public key from OpenSSH encoded data.
    
    :param ssh_public_key_data: OpenSSH public key data in bytes.
    :return: The deserialized public key instance.
    """
    try:
        public_key = serialization.load_ssh_public_key(
            ssh_public_key_data,
            backend=default_backend()
        )
        return public_key
    except ValueError as e:
        raise ValueError(f'Unable to load SSH public key: {e}')

# Example usage
if __name__ == "__main__":
    # Example OpenSSH public key data in bytes (this should be provided)
    ssh_key_data = b"ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEArQ... user@example.com"
    
    # Load the public key
    public_key = load_ssh_public_key(ssh_key_data)
    print(public_key)
