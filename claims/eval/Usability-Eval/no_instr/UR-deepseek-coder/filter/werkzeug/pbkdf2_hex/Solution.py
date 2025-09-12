from werkzeug.security import pbkdf2_hex

def pbkdf2_hex_encoded(password, salt, iterations=100000, keylen=32, hashfunc=None):
    return pbkdf2_hex(password, salt, iterations, keylen, hashfunc)
