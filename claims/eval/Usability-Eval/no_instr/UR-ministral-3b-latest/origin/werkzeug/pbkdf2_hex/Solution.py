from werkzeug.security import generate_password_hash

# Additional imports
import hashlib

def pbkdf2_bin(password, salt='$2a$12$'):
    """Generate a PBKDF2 hash as a hex-encoded string."""
    # Use werkzeug's password hashing method
    hashed = generate_password_hash(password)

    # Convert the hash to bytes
    bytes_hash = hashed.encode('utf-8')

    # Concatenate the salt with the hash as hex-string without the '$'
    salted_hashed = salt + bytes_hash.hex()

    return salted_hashed

# Example usage:
password = "mysecretpassword"
salted_hash = pbkdf2_bin(password)
print(salted_hash)  # This will print a hex-encoded string which is a salted PBKDF2 hash
