from werkzeug.security import generate_password_hash, check_password_hash

def pbkdf2_hash(data, salt, iterations, keylen, hashfunc=None):
    if hashfunc is None:
        hashfunc = hashlib.sha256
    key = generate_password_hash(data, method='pbkdf2', salt=salt, iterations=iterations, keylen=keylen, hashfunc=hashfunc)
    return key
