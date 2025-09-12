from werkzeug import security
import hashlib

def generate_pbkdf2_digest(data, salt, iterations=100000, keylen=32, hashfunc=hashlib.sha256):
    """
    Returns a binary digest for the PBKDF2 hash algorithm of data with the given salt.
    
    Args:
        data (str): The data to be hashed.
        salt (bytes): The salt to use.
        iterations (int): The number of iterations to perform.
        keylen (int): The length of the key to produce.
        hashfunc (hashlib.hash): The hash function to use.

    Returns:
        bytes: The binary digest.
    """
    return security.pbkdf2_bin(
        data, salt, iterations, keylen, hashfunc
    )

# Example usage:
data = "password123"
salt = b"somesalt"
iterations = 100000
keylen = 32
hashfunc = hashlib.sha256

digest = generate_pbkdf2_digest(data, salt, iterations, keylen, hashfunc)
print(digest)
