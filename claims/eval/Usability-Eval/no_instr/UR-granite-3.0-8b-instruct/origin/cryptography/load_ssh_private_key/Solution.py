from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# OpenSSH encoded private key
openssh_private_key = b'-----BEGIN RSA PRIVATE KEY-----\n... (your OpenSSH private key here) ...\n-----END RSA PRIVATE KEY-----'

# Deserialize the private key from OpenSSH encoded data
private_key = serialization.load_pem_private_key(
    openssh_private_key,
    password=None  # If your private key is encrypted, provide the password here
)

# Now you can use the private_key object for encryption, decryption, signing, and verification
