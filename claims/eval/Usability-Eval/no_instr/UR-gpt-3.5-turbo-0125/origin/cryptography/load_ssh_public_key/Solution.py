
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

def deserialize_public_key_from_openssh(public_key_openssh):
    if public_key_openssh.startswith(b"ssh-rsa"):
        algorithm = serialization.NoEncryption()
        return serialization.load_ssh_public_key(public_key_openssh, backend=default_backend()).public_bytes(encoding=serialization.Encoding.OpenSSH, format=serialization.PublicFormat.SubjectPublicKeyInfo)
    else:
        raise ValueError("Unsupported key type")

# Example usage
public_key_openssh = b"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC/... user@domain.com"
deserialized_public_key = deserialize_public_key_from_openssh(public_key_openssh)
print(deserialized_public_key)
