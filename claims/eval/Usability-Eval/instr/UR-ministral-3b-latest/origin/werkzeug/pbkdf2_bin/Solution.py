from werkzeug.security import generate_password_hash

# Example usage
password = "my secret password"
salt = "my salt"
iterations = 100000
key_length = 32

hashed_password = generate_password_hash(password, salt=salt, iterations=iterations, method="pwhash")

print(f"Hashed Password: {hashed_password}")
