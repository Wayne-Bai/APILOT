
import cryptography

# Import the OpenSSH serialization format
from cryptography.hazmat.primitives import serialization

# Define the path to the OpenSSH encoded data
private_key_path = "private_key.pem"

# Read the contents of the private key file
with open(private_KeyPath, "rb") as f:
    private_key_data = f.read()

# Parse the private key using OpenSSH serialization format
serialized_private_key = serialization.load_pem_private_key(
    private_key_data,
    password=None,
    backend=cryptography.hazmat.backends.default_backend()
)

# Get the private key instance from the parsed data
private_key = serialized_private_key.private_key()
