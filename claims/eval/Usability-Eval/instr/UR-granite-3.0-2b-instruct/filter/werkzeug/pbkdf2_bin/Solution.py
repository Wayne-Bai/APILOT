from werkzeug.security import generate_pbkdf2_hash, check_pbkdf2_hash
import hashlib

def generate_pbkdf2_hash_with_hashlib(data, salt, iterations=100000, keylen=32, hashfunc=hashlib.sha256):
    return generate_pbkdf2_hash(data, salt, iterations, keylen, hashfunc)

def check_pbkdf2_hash_with_hashlib(data, salt, hashvalue):
    return check_pbkdf2_hash(data, salt, hashvalue)
