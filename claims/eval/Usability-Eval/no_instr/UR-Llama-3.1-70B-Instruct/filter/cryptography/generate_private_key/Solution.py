# Importing the cryptography library
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

def generate_rsa_private_key():
    """Generate a new RSA private key."""
    
    # Generate a new RSA private key with a key size of 2048 bits and public exponent 65537
    key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )

    # Indentation is just for PEM formatting
    private_pem = key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    ).decode('UTF-8')

    # Print the private key in PEM format
    print(private_pem)

# Generate and print the RSA private key
generate_rsa_private_key()
