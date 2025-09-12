from cryptography.hazmat.primitives.serialization import load_ssh_private_key
from cryptography.hazmat.backends import default_backend

def deserialize_ssh_private_key(ssh_private_key_data, password=None):
    # The password must be bytes, if provided
    if password:
        password = password.encode()

    private_key = load_ssh_private_key(
        ssh_private_key_data.encode(),
        password=password,
        backend=default_backend()
    )

    return private_key

# Example usage:
# Assuming you have your SSH private key data as a string and password if it is encrypted
ssh_private_key_data = """
-----BEGIN OPENSSH PRIVATE KEY-----
...
-----END OPENSSH PRIVATE KEY-----
"""

password = "your_password_here"  # None if the key is not password-protected

private_key = deserialize_ssh_private_key(ssh_private_key_data, password)
print(private_key)
