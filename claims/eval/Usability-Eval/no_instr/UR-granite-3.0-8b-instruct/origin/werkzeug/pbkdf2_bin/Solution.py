from werkzeug.security import generate_password_hash, check_password_hash
import hashlib

def generate_pbkdf2_hash(data, salt, iterations, keylen, hashfunc=hashlib.sha256):
    if len(salt) != keylen:
        raise ValueError("Salt must be exactly {} bytes long".format(keylen))

    pbkdf2_hash = hashlib.pbkdf2_hmac(hashfunc(), salt, iterations, keylen)
    return pbkdf2_hash

# Example usage:
data = b"my_secret_data"
salt = b"my_random_salt"
iterations = 1000
keylen = 32

hash = generate_pbkdf2_hash(data, salt, iterations, keylen)
print(hash)
