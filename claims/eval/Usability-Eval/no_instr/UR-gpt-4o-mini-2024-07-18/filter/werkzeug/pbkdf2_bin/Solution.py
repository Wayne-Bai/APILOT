from werkzeug.security import generate_password_hash, check_password_hash
import hashlib

def pbkdf2_hash(data, salt, iterations=100000, keylen=32, hashfunc=hashlib.sha256):
    """Returns a binary digest for the PBKDF2 hash algorithm of data with the given salt."""
    return hashlib.pbkdf2_hmac(hashfunc().name, data.encode(), salt.encode(), iterations, dklen=keylen)

# Example usage:
data = 'my_secret_password'
salt = 'random_salt'
hashed_password = pbkdf2_hash(data, salt)
print(hashed_password)
