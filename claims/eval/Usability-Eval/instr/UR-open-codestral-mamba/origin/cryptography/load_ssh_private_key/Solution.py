from cryptography.hazmat.primitives import serialization

def deserialize_private_key(private_key_openssh: bytes, password: bytes):
    try:
        private_key_encrypt = serialization.load_ssh_private_key(private_key_openssh, password)
        return private_key_encrypt
    except Exception as e:
        print(f"Failed to deserialize the private key: {str(e)}")
        return None
