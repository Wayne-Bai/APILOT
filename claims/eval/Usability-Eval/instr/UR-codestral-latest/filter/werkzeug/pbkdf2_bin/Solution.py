import hashlib
import binascii
from werkzeug.security import pbkdf2_hex

def generate_pbkdf2_hash(data, salt, iterations=100000, keylen=24, hashfunc=None):
    if hashfunc is None:
        hashfunc = hashlib.sha256
    return binascii.unhexlify(pbkdf2_hex(data, salt, iterations, keylen, hashfunc))
