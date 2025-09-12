from werkzeug.security import generate_password_hash

def pbkdf2_hex(password: str, salt: str, iterations: int = 100000) -> str:
    """Generate a PBKDF2 hash in hex format."""
    return generate_password_hash(password, method='pbkdf2:sha256', salt=salt, iterations=iterations)

# Example usage
password = "my_secure_password"
salt = "random_salt"
hashed_password = pbkdf2_hex(password, salt)
print(hashed_password)
