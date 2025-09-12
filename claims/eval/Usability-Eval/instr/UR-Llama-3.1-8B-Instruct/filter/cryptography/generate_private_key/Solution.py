from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
import os

def generate_private_key():
    """
    Generates a new RSA private key.
    
    Returns:
        str: The PEM format private key.
    """
    # Generate a new RSA key pair
    key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    
    # Get the private bytes
    private_bytes = key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    
    # Return the private key as a string
    return private_bytes.decode('utf-8')

# Generate a new RSA private key
private_key = generate_private_key()
print(private_key)
