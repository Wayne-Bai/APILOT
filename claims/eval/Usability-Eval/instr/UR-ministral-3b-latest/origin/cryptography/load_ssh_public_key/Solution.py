from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import load_pem_public_key

# Sample OpenSSH encoded public key
ssh_public_key = b"ssh-rsa AAAAB...content"

# Load PEM formatted public key
public_key_data = ssh_public_key  # This would be your full PEM encoded data

# Deserialize to RSA public key instance
public_key = load_pem_public_key(
    public_key_data,
    backend=default_backend()
)

# Now you can use the `public_key` as needed in your application
