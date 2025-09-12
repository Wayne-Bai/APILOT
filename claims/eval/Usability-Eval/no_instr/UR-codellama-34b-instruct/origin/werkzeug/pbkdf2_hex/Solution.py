
from werkzeug.security import generate_password_hash, check_password_hash

def pbkdf2_hex(password, salt):
    """
    Generate a hex-encoded string using the pbkdf2 key derivation function.
    """
    hash = generate_password_hash(password, salt)
    return hash.hex()
