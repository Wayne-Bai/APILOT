
from hashlib import pbkdf2_hmac

def generate_pbkdf2_hash(data, salt, iterations, keylen, hashfunc='sha256'):
    key = pbkdf2_hmac(hashfunc, data.encode(), salt.encode(), iterations, keylen)
    return key

# Example usage
data = "password123"
salt = "somesalt"
iterations = 1000
keylen = 32

hashed_key = generate_pbkdf2_hash(data, salt, iterations, keylen)
print(hashed_key.hex())
