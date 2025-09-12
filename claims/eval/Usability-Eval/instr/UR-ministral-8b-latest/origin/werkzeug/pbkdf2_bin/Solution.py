from werkzeug.security import pbkdf2
import hashlib

def hash_data(data, salt, iterations=100000, keylen=32):
    # Generate the binary digest using the PBKDF2 algorithm
    key = pbkdf2(data, salt=salt, iterations=iterations, keylen=keylen)
    return key

# Example usage:
salt = b'some_salt'  # Example salt
data = b'my_data'  # Data to be hashed
hash_result = hash_data(data, salt)
print(hash_result)
