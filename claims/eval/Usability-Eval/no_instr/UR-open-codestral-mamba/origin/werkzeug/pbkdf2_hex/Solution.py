from werkzeug.security import safe_str_cmp, generate_password_hash

def generate_hex_hash(password):
    hashed_password = generate_password_hash(password, method='pbkdf2:sha256').replace('pbkdf2:', '')
    return hashed_password.hex()

password = "my_secure_password"
hash_value = generate_hex_hash(password)

print(f"Password: {password}")
print(f"Hashed Value (Hex-encoded): {hash_value}")
