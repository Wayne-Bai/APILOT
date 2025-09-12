from werkzeug.security import generate_password_hash

def pbkdf2_hex(string, salt, iterations=100000, key_length=64):
    method = f"pbkdf2:sha256:{iterations}"
    # Generate password hash
    hash_value = generate_password_hash(string, method=method, salt_length=len(salt))
    # Extract the hex-encoded hash part
    hex_encoded = hash_value.split('$')[-1]
    return hex_encoded

# Example Usage:
hashed_value = pbkdf2_hex('my_password', 'my_salt')
print(hashed_value)
