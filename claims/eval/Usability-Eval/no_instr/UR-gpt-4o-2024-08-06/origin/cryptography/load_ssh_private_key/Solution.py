from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

# Example OpenSSH encoded private key
openssh_private_key_data = b"""
-----BEGIN OPENSSH PRIVATE KEY-----
...
-----END OPENSSH PRIVATE KEY-----
"""

# Deserialize the private key
private_key = serialization.load_ssh_private_key(
    openssh_private_key_data,
    password=None,  # You can replace None with a bytes password if the key is encrypted
    backend=default_backend()
)

# Now private_key is an instance of the private key type
print(f"Deserialized private key: {private_key}")
