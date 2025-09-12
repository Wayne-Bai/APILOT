from werkzeug.security import generate_password_hash

# Sample password
password = "my_secure_password"

# Generate a hex-encoded PBKDF2 hash
hex_hash = generate_password_hash(password, algorithm='pbkdf2_sha256').hex()

print(f"Hex-encoded PBKDF2 hash: {hex_hash}")
