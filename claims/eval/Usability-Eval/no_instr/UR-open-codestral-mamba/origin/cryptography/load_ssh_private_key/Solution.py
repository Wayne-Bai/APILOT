from cryptography.hazmat.primitives.asymmetric import serialization
from cryptography.hazmat.primitives import serialization as crypto_serialization
from cryptography.hazmat.backends import default_backend as crypto_default_backend

def deserialize_openssh_key(ssh_key):
    private_bytes = crypto_serialization.load_ssh_private_key(ssh_key.encode(), password=None)
    private_key = serialization.load_pem_private_key(private_bytes, password=None, backend=crypto_default_backend())
    return private_key

# Test the function
ssh_key = "-----BEGIN OPENSSH PRIVATE KEY-----...-----END OPENSSH PRIVATE KEY-----"
private_key = deserialize_openssh_key(ssh_key)
print(private_key)
