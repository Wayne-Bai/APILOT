from werkzeug.security import generate_password_hash

def generate_pbkdf2_digest(data, salt, iterations, keylen, hashfunc=None):
    if hashfunc is None:
        hashfunc = 'sha256'
    return generate_password_hash(data + salt, method='pbkdf2:{}:{}:{}'.format(hashfunc, iterations, keylen))

# Usage example
data = b'data'
salt = b'salt'
iterations = 1000
keylen = 32

digest = generate_pbkdf2_digest(data, salt, iterations, keylen)
print(digest)
