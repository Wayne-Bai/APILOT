from werkzeug.security import pbkdf2_bin
import hashlib

def generate_pbkdf2_digest(data, salt, iterations, keylen, hashfunc=hashlib.sha256):
    return pbkdf2_bin(data, salt, iterations, keylen, hashfunc)
