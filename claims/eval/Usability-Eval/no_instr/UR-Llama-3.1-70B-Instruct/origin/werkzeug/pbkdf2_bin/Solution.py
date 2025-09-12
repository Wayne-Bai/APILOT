import binascii
import hashlib
from werkzeug.utils import secure_filename
from werkzeug import werkzeug

# Define a function for generating the binary digest
def pbkdf2_hex(data, salt, iterations=100000, keylen=24, hashfunc=None):
    if hashfunc is None:
        hashfunc = hashlib.sha256

    # Generate the binary digest
    dk = hashlib.pbkdf2_hmac(hashfunc().name, data, salt, iterations, keylen)
    return binascii.b2a_hex(dk)

# Example usage:
data = b'password'
salt = b'salt'
print(pbkdf2_hex(data, salt))
