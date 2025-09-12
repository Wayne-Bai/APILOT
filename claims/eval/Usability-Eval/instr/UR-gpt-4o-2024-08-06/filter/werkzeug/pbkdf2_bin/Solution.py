from werkzeug.security import generate_password_hash
import hashlib
import hmac
import os

def pbkdf2_digest(data, salt, iterations=100000, keylen=32, hashfunc=hashlib.sha256):
    salt = bytes(salt, 'utf-8')
    data = bytes(data, 'utf-8')
    
    dk = hashlib.pbkdf2_hmac(
        hashfunc().name,
        data,
        salt,
        iterations,
        dklen=keylen
    )
    return dk

# Example usage:
data = "password"
salt = "salt"
iterations = 100000
keylen = 32

binary_digest = pbkdf2_digest(data, salt, iterations, keylen)
print(binary_digest)
