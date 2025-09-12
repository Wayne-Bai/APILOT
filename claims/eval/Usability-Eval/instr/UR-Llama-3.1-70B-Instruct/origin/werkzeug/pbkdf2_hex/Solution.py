# Importing the necessary libraries
import secrets
from Crypto.Hash import SHA256
from Crypto.Protocol.KDF import PBKDF2

def generate_hex_encoded_hash(password, salt=None, iterations=100000):
    """
    Generates a hex-encoded PBKDF2 hash.

    Args:
        password (str): The password to be hashed.
        salt (bytes, optional): The salt to be used. Defaults to None, which will generate a random salt.
        iterations (int, optional): The number of iterations for the hash. Defaults to 100000.

    Returns:
        tuple: A tuple containing the hex-encoded salt and the hex-encoded hash.
    """
    # Generate a random salt if none is provided
    if salt is None:
        salt = secrets.token_bytes(16)
    
    # Generate the hash using PBKDF2 with SHA256 as the hash function
    key = PBKDF2(password, salt, 32, iterations=iterations, hmac_hash_module=SHA256)

    # Return the hex-encoded salt and hash
    return salt.hex(), key.hex()

# Example usage:
password = "mysecretpassword"
salt, hash = generate_hex_encoded_hash(password)

print("Salt:", salt)
print("Hash:", hash)
