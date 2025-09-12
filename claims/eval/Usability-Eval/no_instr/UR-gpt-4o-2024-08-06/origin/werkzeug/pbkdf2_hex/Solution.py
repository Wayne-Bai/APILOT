from werkzeug.security import pbkdf2_hex

def generate_hex_key(password: str, salt: str, iterations: int = 100000, key_length: int = 32, hash_name: str = 'sha256') -> str:
    """
    Generates a hex-encoded key derived from the password, using PBKDF2.

    :param password: The password to derive the key from.
    :param salt: The salt to use.
    :param iterations: Number of iterations to perform (default is 100000).
    :param key_length: Length of the derived key in bytes (default is 32).
    :param hash_name: Name of the hash function to use (default is 'sha256').
    :return: A hex-encoded string representing the derived key.
    """
    derived_key = pbkdf2_hex(password, salt, iterations, key_length, hash_name)
    return derived_key

# Example usage
password = 'mysecretpassword'
salt = 'somesalt'
hex_key = generate_hex_key(password, salt)
print(hex_key)
