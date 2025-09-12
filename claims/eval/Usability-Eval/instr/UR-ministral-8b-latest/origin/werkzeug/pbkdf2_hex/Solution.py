from werkzeug.security import generate_password_hash

# Function to hash a password
def hash_password(password):
    return generate_password_hash(password)

# Example usage
password = "user_password"
hash = hash_password(password)
print(f"Hashed password: {hash}")
