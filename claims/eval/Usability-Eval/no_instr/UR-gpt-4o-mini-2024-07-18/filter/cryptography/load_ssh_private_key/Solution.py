from cryptography.hazmat.primitives import serialization

# Example: Deserialize a private key from OpenSSH encoded data
openssh_private_key = b"""
-----BEGIN OPENSSH PRIVATE KEY-----
<YOUR_OPENSSH_PRIVATE_KEY_HERE>
-----END OPENSSH PRIVATE KEY-----
"""

# Load the private key
private_key = serialization.load_ssh_private_key(
    openssh_private_key,
    password=None  # Provide a password if the key is encrypted
)

# Now `private_key` is an instance of the private key type
