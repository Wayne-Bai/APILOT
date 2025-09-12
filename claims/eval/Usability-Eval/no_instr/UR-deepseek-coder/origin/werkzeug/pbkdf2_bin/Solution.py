from werkzeug.security import pbkdf2_bin
import hashlib

def generate_pbkdf2_hash(data, salt, iterations=100000, keylen=32, hashfunc=hashlib.sha256):
    """
    Returns a binary digest for the PBKDF2 hash algorithm of data with the given salt.
    It iterates iterations times and produces a key of keylen bytes.
    By default, SHA-256 is used as hash function; a different hashlib hashfunc can be provided.
    """
    return pbkdf2_bin(data, salt, iterations, keylen, hashfunc)
