
from werkzeug.security import pbkdf2_bin
import binascii

def pbkdf2_hex(password, salt, iterations=1000, keylen=24, hashfunc=None):
    if hashfunc is None:
        hashfunc = 'sha512'
    key = pbkdf2_bin(password, salt, iterations, keylen, hashfunc)
    return binascii.hexlify(key).decode('utf-8')
