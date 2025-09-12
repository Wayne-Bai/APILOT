from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
import os

# Function to generate DSA private key
def generate_dsa_private_key():
    # Create a new RSA key pair
    key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    
    # Get the private bytes from the key
    private_pem = key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )
    
    return private_pem

# Generate a new DSA private key
private_key = generate_dsa_private_key()

# Save the private key to a file
with open('dsa_private_key.pem', 'wb') as f:
    f.write(private_key)
