from werkzeug.security import generate_password_hash

def pbkdf2_hex(password, salt, iterations=100000, key_length=None, hash_name='sha256'):
    if key_length is None:
        key_length = hash_name in ('sha224', 'sha256', 'sha384', 'sha512', 'md5', 'sha1') and 24 or 64
    hash_value = generate_password_hash(password + salt, method=f'pbkdf2:{hash_name}', salt_length=len(salt), iterations=iterations)
    # Extract just the hash hex part
    return hash_value.split('$')[-1]

# Usage
hashed_password = pbkdf2_hex('secure_password', 'random_salt')
print(hashed_password)
