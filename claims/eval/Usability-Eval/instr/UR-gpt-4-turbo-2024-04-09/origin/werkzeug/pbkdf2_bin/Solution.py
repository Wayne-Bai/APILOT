from werkzeug.security import generate_password_hash

def pbkdf2_hash(data, salt, iterations, keylen, hashfunc='sha256'):
    # Generating the hash using PBKDF2
    hash_value = generate_password_hash(
        password=data,
        method=f'pbkdf2:{hashfunc}',
        salt_length=len(salt),
        iterations=iterations
    )
    # Returning the part of the hash that represents the PBKDF2 digest, truncated to keylen bytes.
    return hash_value.encode()[:keylen]

# Example of using the function
data = "example_data"
salt = "example_salt"
iterations = 100000
keylen = 32

hashed_data = pbkdf2_hash(data, salt, iterations, keylen)
print(hashed_data)
