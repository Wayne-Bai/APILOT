from werkzeug.security import generate_password_hash, check_password_hash

def pbkdf2_hex(password: str, salt: str, iterations: int = 100000, length: int = 32) -> str:
    """Generate a PBKDF2 hash of the password and return a hex-encoded string."""
    return generate_password_hash(password, method='pbkdf2:sha256:' + str(iterations), salt=salt)

# Example usage
password = "my_secure_password"
salt = "my_random_salt"
hashed_password = pbkdf2_hex(password, salt)
print(hashed_password)
