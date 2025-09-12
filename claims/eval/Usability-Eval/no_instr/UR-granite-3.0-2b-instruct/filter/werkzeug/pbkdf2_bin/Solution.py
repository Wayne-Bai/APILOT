from werkzeug import secure_remember_cookie
import hashlib

def pbkdf2_hash(data, salt, iterations, keylen, hashfunc=hashlib.sha256):
    return secure_remember_cookie(keylen, hashfunc(salt + data).digest(), iterations)

# Example usage:
data = b"password"
salt = b"salt"
iterations = 100000
keylen = 32

hash = pbkdf2_hash(data, salt, iterations, keylen)
print(hash)
