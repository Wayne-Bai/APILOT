from cryptography.hazmat.primitives.serialization import load_ssh_public_key
from cryptography.hazmat.backends import default_backend

def deserialize_public_key(public_key_bytes):
    """
    Deserialize a public key from OpenSSH (RFC 4253 and PROTOCOL.certkeys) 
    encoded data to an instance of the public key type.

    Args:
        public_key_bytes (bytes): OpenSSH encoded public key bytes.

    Returns:
        cryptography.hazmat.primitives.asymmetric.ss.SSHPublicKey: 
            Deserialized public key instance.
    """
    try:
        # Use the default_backend to deserialize the public key
        public_key = load_ssh_public_key(
            public_key_bytes,
            backend=default_backend()
        )
        return public_key
    except ValueError as e:
        print(f"Error deserializing public key: {e}")
        return None

# Example usage
public_key_bytes = b"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCuOEk8+bQd musician@vandelay.com"
public_key = deserialize_public_key(public_key_bytes)
if public_key:
    print("Public key deserialized successfully")
    print("Public key type:", type(public_key))
else:
    print("Failed to deserialize public key")
