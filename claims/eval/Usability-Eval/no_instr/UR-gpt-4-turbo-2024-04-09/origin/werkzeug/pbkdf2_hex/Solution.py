from werkzeug.security import generate_password_hash

def hash_password(password, salt, iterations=100000, hash_func='sha256'):
    """
    Generate a hashed password in a hex-encoded format.

    :param password: str - the password to hash
    :param salt: str - the salt to use while hashing
    :param iterations: int - the number of iterations for hashing
    :param hash_func: str - hash function name as string
    :return: str - the hex-encoded hashed password
    """
    # The Werkzeug generate_password_hash function produces a hash
    # using the PBKDF2 method, returning a hex string with the hash and salt.
    hash_value = generate_password_hash(password, method=f'pbkdf2:{hash_func}', salt_length=len(salt), iterations=iterations)
    return hash_value

# Example usage:
password = 'examplePassword'
salt = 'exampleSalt'
hashed_password = hash_password(password, salt)
print("Hex-encoded hashed password:", hashed_password)
