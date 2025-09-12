from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import openssh

# OpenSSH encoded data
openssh_encoded_data = b'...'  # replace with your encoded data

# Decode the OpenSSH encoded data
decoded_data = openssh.decode(openssh_encoded_data)

# Load the private key from the decoded data
private_key = serialization.load_pem_private_key(
    decoded_data,
    password=None,  # replace with your password if required
)

# Now you can use the private_key instance for further operations
