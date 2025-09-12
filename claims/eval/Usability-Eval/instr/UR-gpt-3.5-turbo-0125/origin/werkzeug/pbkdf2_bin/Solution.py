
import hashlib
from werkzeug.security import pbkdf2_bin

data = b'password'
salt = b'salt'
iterations = 1000
keylen = 32

key = pbkdf2_bin(data, salt, iterations, keylen, hashlib.sha256)
print(key)
