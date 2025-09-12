from werkzeug.security import generate_password_hash

def hash_pbkdf2(data, salt, iterations=100000, keylen=32, hashfunc=None):
    if hashfunc:
        from hashlib import new
        hashfunc = new(hashfunc)
    else:
        from hashlib import sha256 as hashfunc
    return generate_password_hash(data.encode('utf-8'), method='pbkdf2', salt=salt, iterations=iterations, hashfunc=hashfunc, keylen=keylen)

# Example usage
hash_pbkdf2("my_float_compusld_pwpwd", "m6HsJUoeSmminPqyQjy1j3")
