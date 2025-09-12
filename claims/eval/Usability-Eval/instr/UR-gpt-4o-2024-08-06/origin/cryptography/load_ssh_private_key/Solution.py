from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

# OpenSSH private key data as a byte string
private_key_data = b"""
-----BEGIN OPENSSH PRIVATE KEY-----
...
-----END OPENSSH PRIVATE KEY-----
"""

# Load the private key from the OpenSSH encoded data
private_key = serialization.load_ssh_private_key(
    private_key_data,
    password=None,  # Use a byte string password if the key is encrypted
    backend=default_backend()
)

# The `private_key` variable now holds the deserialized private key instance
