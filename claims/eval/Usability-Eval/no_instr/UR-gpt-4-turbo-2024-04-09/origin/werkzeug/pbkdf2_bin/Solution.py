import werkzeug.security

def get_pbkdf2_hash(data, salt, iterations, keylen, hashfunc=None):
    return werkzeug.security.pbkdf2_bin(data, salt, iterations=iterations, keylength=keylen, hashfunc=hashfunc)

# Example usage
data = "password"
salt = "somesalt"
iterations = 10000
keylen = 24

hash_result = get_pbkdf2_hash(data, salt, iterations, keylen)
print(hash_result)
