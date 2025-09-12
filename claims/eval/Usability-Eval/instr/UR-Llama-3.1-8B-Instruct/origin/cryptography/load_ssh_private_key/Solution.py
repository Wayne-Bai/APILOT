# Import required modules from the cryptography library
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import load_pem_private_key

# Define a function to deserialize a private key from OpenSSH encoded data
def deserialize_private_key(open_ssh_encoded_data):
    # Convert OpenSSH encoded data to pem encoded data
    pem_encoded_data = open_ssh_encoded_data.replace("-----BEGIN OPENSSH PRIVATE KEY-----", "").replace("-----END OPENSSH PRIVATE KEY-----", "").replace("\n", "")
    
    # Load the private key from the pem encoded data
    try:
        private_key = load_pem_private_key(
            pem_encoded_data.encode(),
            password=None,
            backend=default_backend(),
        )
    except ValueError as e:
        raise ValueError(f"Failed to deserialize private key: {e}")
    
    return private_key

# Example usage:
open_ssh_encoded_data = """
-----BEGIN OPENSSH PRIVATE KEY-----
[redacted OpenSSH encoded data]
-----END OPENSSH PRIVATE KEY-----
"""

try:
    private_key = deserialize_private_key(open_ssh_encoded_data)
    print(private_key)
except ValueError as e:
    print(e)
