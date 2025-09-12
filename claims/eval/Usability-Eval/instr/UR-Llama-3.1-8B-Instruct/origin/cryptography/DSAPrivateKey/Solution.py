from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

def generate_private_key(key_size=2048):
    """
    Generate a new RSA private key.

    Args:
        key_size (int): The size of the key in bits.

    Returns:
        A PrivateKey instance from the cryptography library.
    """
    # Generate a new RSA private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=key_size,
        backend=default_backend()
    )

    # Serialize the private key
    private_key_bytes = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )

    return private_key, private_key_bytes


# Generate a 2048-bit private key
private_key, private_key_bytes = generate_private_key(2048)

# Print the private key
print("Private Key:")
print(private_key_bytes.decode("utf-8"))

# Convert the private key bytes to a string that can be stored securely
private_key_string = private_key_bytes.decode("utf-8")

# Store the private key securely (e.g., encrypt it and store it on disk)
# Remember to replace "secure_storage" with your actual secure storage method
# secure_storage.store(private_key_string)

# Example using environment variables to store the private key securely
import os
os.environ['PRIVATE_KEY'] = private_key_string
