
from werkzeug.security import generate_password_hash

def get_pbkdf2_digest(data, salt, iterations, keylen, hashfunc=None):
    if hashfunc is None:
        hashfunc = generate_password_hash()
    return hashfunc.pbkdf2_digest(data, salt, iterations, keylen)
