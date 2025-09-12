from werkzeug.security import pbkdf2_bin
import hashlib

def get_pbkdf2_digest(data, salt, iterations=100000, keylen=32, hashfunc=hashlib.sha256):
    """
    Returns a binary digest for the PBKDF2 hash algorithm of data with the given salt.

    :param data: The data to be hashed
    :param salt: The salt to be used in hashing
    :param iterations: The number of iterations to perform (default: 100000)
    :param keylen: The length of the derived key in bytes (default: 32)
    :param hashfunc: The hash function to use (default: hashlib.sha256)
    :return: The binary digest
    """
    return pbkdf2_bin(data, salt, iterations=iterations, keylen=keylen, hashfunc=hashfunc)

# Example usage
data = b'my secret data'
salt = b'secret_salt'
digest = get_pbkdf2_digest(data, salt)
print(digest)
